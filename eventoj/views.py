import json
from unidecode import unidecode
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.views import generic
from django.db import transaction
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .forms import (ArangxoForm, EventoCreateForm,  EventoForm,
                    RenkontigxoForm)
from .models import Arangxo, Evento


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        if 'object' in context:
            context = context['object'].as_dict()
        if 'object_list' in context:
            context = [obj.as_dict() for obj in context['object_list']]
        return json.dumps(context, ensure_ascii=False)


class EventoJSONListView(JSONResponseMixin, generic.list.BaseListView):
    model = Evento

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super(EventoJSONListView, self).dispatch(request,
                                                        *args, **kwargs)

    def get_queryset(self):
        args = self.request.GET
        n, s, e, w = args['n'], args['s'], args['e'], args['w']
        qs = Evento.objects.filter(long__lte=n).filter(long__gte=s).filter(
            lat__gte=w).filter(lat__lte=e)
        return qs

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

evento_json_list = EventoJSONListView.as_view()


class RenkontigxoCreateView(LoginRequiredMixin, generic.FormView):
    form_class = RenkontigxoForm
    template_name = 'eventoj/renkontigxo_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(RenkontigxoCreateView, self).dispatch(request,
                                                           *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RenkontigxoCreateView, self).get_context_data(**kwargs)
        context['object_list'] = Arangxo.objects.all()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            nomo = form.cleaned_data['nomo']
            mallonga_nomo = form.cleaned_data['mallonga_nomo']
            arangxo_nomo = Arangxo.objects.filter(nomo__iexact=nomo)
            arangxo_mallonga_nomo = Arangxo.objects.filter(
                mallonga_nomo__iexact=mallonga_nomo)
            if arangxo_nomo:
                self.arangxo = arangxo_nomo[0]
            elif arangxo_mallonga_nomo:
                self.arangxo = arangxo_mallonga_nomo[0]
            else:
                self.arangxo = Arangxo.objects.create(
                    kreanto=self.user,
                    nomo=form.cleaned_data['nomo'],
                    mallonga_nomo=form.cleaned_data['mallonga_nomo'],
                    min_homoj=form.cleaned_data['min_homoj'],
                    max_homoj=form.cleaned_data['max_homoj'],
                    publiko=form.cleaned_data['publiko'],
                )
            self.evento = Evento.objects.create(
                arangxo=self.arangxo,
                kreanto=self.user,
                komenco=form.cleaned_data['komenco'],
                fino=form.cleaned_data['fino'],
                lat=form.cleaned_data['lat'],
                long=form.cleaned_data['long'],
                temo=form.cleaned_data['temo'],
                urbo=form.cleaned_data['urbo'],
                posxtkodo=form.cleaned_data['posxtkodo'],
                lando=form.cleaned_data['lando'],
                priskribo=form.cleaned_data['priskribo'],
            )
            self.arangxo.etikedoj.add(*form.cleaned_data['etikedoj'])
            return super(RenkontigxoCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('evento_detail', kwargs={
            'slug': self.arangxo.slug,
            'jaro': self.evento.jaro,
            'monato': self.evento.monato,
            'tago': self.evento.tago,
        })

evento_arangxo_create = RenkontigxoCreateView.as_view()


class ArangxoListView(generic.ListView):
    model = Arangxo

arangxo_list = ArangxoListView.as_view()


class ArangxoDetailView(generic.DetailView):
    model = Arangxo

arangxo_detail = ArangxoDetailView.as_view()


class ArangxoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Arangxo
    form_class = ArangxoForm

    def get_success_url(self):
        return reverse('arangxo_detail', args=[self.object.slug])

arangxo_create = ArangxoCreateView.as_view()


class ArangxoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Arangxo
    form_class = ArangxoForm

    def get_success_url(self):
        return reverse('arangxo_detail', args=[self.object.slug])

arangxo_update = ArangxoUpdateView.as_view()


class EventoListView(generic.ListView):
    model = Evento

evento_list = EventoListView.as_view()


class EventoDetailView(generic.DetailView):
    model = Evento

    def dispatch(self, request, *args, **kwargs):
        self.slug = kwargs.pop('slug')
        self.jaro = kwargs.pop('jaro')
        self.monato = kwargs.pop('monato')
        self.tago = kwargs.pop('tago')
        if self.get_object() is None:
            return redirect('arangxo_detail', slug=self.slug)
        return super(EventoDetailView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        queryset = Evento.objects.filter(arangxo__slug=self.slug)
        if self.jaro:
            queryset = queryset.filter(komenco__year=self.jaro)
        if self.monato:
            queryset = queryset.filter(komenco__month=self.monato)
        if self.tago:
            queryset = queryset.filter(komenco__day=self.tago)

        if queryset.count() == 1:
            return queryset[0]
        elif queryset.count() == 0:
            raise Http404
        else:
            return None

evento_detail = EventoDetailView.as_view()


class EventoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Evento
    form_class = EventoCreateForm

    def dispatch(self, request, *args, **kwargs):
        self.slug = kwargs['slug']
        self.user = request.user
        return super(EventoCreateView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(EventoCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['arangxo'] = self.slug
        return kwargs

    def get_success_url(self):
        return reverse('evento_detail', kwargs={
            'slug': self.object.arangxo.slug,
            'jaro': self.object.jaro,
            'monato': self.object.monato,
            'tago': self.object.tago,
        })

evento_create = EventoCreateView.as_view()


class EventoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Evento
    form_class = EventoForm

    def dispatch(self, request, *args, **kwargs):
        self.slug = kwargs.pop('slug')
        self.jaro = kwargs.pop('jaro')
        self.monato = kwargs.pop('monato')
        self.tago = kwargs.pop('tago')
        if self.get_object() is None:
            return redirect('arangxo_detail', slug=self.slug)
        return super(EventoUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        queryset = Evento.objects.filter(arangxo__slug=self.slug)
        if self.jaro:
            queryset = queryset.filter(komenco__year=self.jaro)
        if self.monato:
            queryset = queryset.filter(komenco__month=self.monato)
        if self.tago:
            queryset = queryset.filter(komenco__day=self.tago)

        if queryset.count() == 1:
            return queryset[0]
        elif queryset.count() == 0:
            raise Http404
        else:
            return None

    def get_success_url(self):
        return reverse('evento_detail', kwargs={
            'slug': self.object.arangxo.slug,
            'jaro': self.object.jaro,
            'monato': self.object.monato,
            'tago': self.object.tago,
        })

evento_update = EventoUpdateView.as_view()
