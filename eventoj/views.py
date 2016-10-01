import json
from urllib.parse import urlencode

from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.views import generic
from django.db import transaction
from django.db.models import Q
from django.shortcuts import redirect

from rest_framework import viewsets
from braces.views import LoginRequiredMixin

from .forms import (ArangxoForm, EventoCreateForm,  EventoForm,
                    RenkontigxoNomoForm, RenkontigxoForm)
from .models import Arangxo, Evento
from .serializers import EventoSerializer, ArangxoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class ArangxoViewSet(viewsets.ModelViewSet):
    queryset = Arangxo.objects.all()
    serializer_class = ArangxoSerializer


def get_arangxoj(nomo, mallonga_nomo=''):
    if mallonga_nomo:
        query = Q(nomo__icontains=nomo) | \
                Q(mallonga_nomo__icontains=mallonga_nomo)
    else:
        query = Q(nomo__icontains=nomo)

    return Arangxo.objects.filter(query)


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


class EventoJunularaListView(generic.ListView):
    model = Evento
    template_name = 'eventoj/junulara_list.html'

    def get_queryset(self):
        queryset = super(EventoJunularaListView, self).get_queryset()
        return queryset.filter(arangxo__publiko=3).order_by('-komenco')

evento_junulara_list = EventoJunularaListView.as_view()


class EventoJSONListView(JSONResponseMixin, generic.list.BaseListView):
    model = Evento

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        _publiko = request.GET.get('publiko', '')
        try:
            self.publiko = int(_publiko) if 0 <= int(_publiko) < 5 else None
        except ValueError:
            _publiko = request.GET.get('publiko', '').upper()
            self.publiko = getattr(Arangxo.PUBLIKO_ELEKTOJ, _publiko, None)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        args = self.request.GET
        n, s, e, w = args.get('n', ''), args.get('s', ''), args.get('e', ''), args.get('w', '')
        qs = Evento.objects.filter(long__lte=n, long__gte=s,
                                   lat__gte=w, lat__lte=e)
        qs = qs.filter(fino__gte=now())
        if self.publiko is not None:
            qs = qs.filter(arangxo__publiko=self.publiko)
        return qs

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

evento_json_list = EventoJSONListView.as_view()


class RenkontigxoNomoFormView(LoginRequiredMixin, generic.FormView):
    form_class = RenkontigxoNomoForm
    template_name = 'eventoj/renkontigxo_nomo_form.html'

    def form_valid(self, form):
        self.nomo = form.cleaned_data['nomo']
        self.mallonga_nomo = form.cleaned_data['mallonga_nomo']
        return super(RenkontigxoNomoFormView, self).form_valid(form)

    def get_success_url(self):
        args = {'nomo': self.nomo.encode('utf8')}
        if self.mallonga_nomo:
            args['mallonga_nomo'] = self.mallonga_nomo.encode('utf8')

        if get_arangxoj(self.nomo, self.mallonga_nomo):
            return reverse('cxu_nova_arangxo') + '?' + urlencode(args)
        else:
            return reverse('renkontigxo_create') + '?' + urlencode(args)

renkontigxo_nomo_create = RenkontigxoNomoFormView.as_view()


class CxuNovaArangxo(LoginRequiredMixin, generic.ListView):
    model = Arangxo
    template_name = 'eventoj/cxu_nova_arangxo.html'

    def get_queryset(self, *args, **kwargs):
        self.nomo = self.request.GET.get('nomo', '')
        self.mallonga_nomo = self.request.GET.get('mallonga_nomo', '')
        return get_arangxoj(self.nomo, self.mallonga_nomo)

cxu_nova_arangxo = CxuNovaArangxo.as_view()


class RenkontigxoCreateView(LoginRequiredMixin, generic.FormView):
    form_class = RenkontigxoForm
    template_name = 'eventoj/renkontigxo_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(RenkontigxoCreateView, self).dispatch(request,
                                                           *args, **kwargs)

    def get_initial(self):
        return self.request.GET

    def get_context_data(self, **kwargs):
        context = super(RenkontigxoCreateView, self).get_context_data(**kwargs)
        context['object_list'] = Arangxo.objects.all()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            nomo = form.cleaned_data['nomo']
            mallonga_nomo = form.cleaned_data['mallonga_nomo']
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
                kioma=form.cleaned_data['kioma'],
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

renkontigxo_create = RenkontigxoCreateView.as_view()


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

    def get_context_data(self, **kwargs):
        context = super(EventoCreateView, self).get_context_data(**kwargs)
        context['arangxo'] = Arangxo.objects.get(slug=self.slug)
        return context

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
