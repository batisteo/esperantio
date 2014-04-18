from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.db import transaction

from braces.views import LoginRequiredMixin

from .forms import (ArangxoForm, EventoCreateForm,  EventoForm,
        RenkontigxoForm)
from .models import Arangxo, Evento


class RenkontigxoCreateView(LoginRequiredMixin, generic.FormView):
    form_class = RenkontigxoForm
    template_name = 'eventoj/renkontigxo_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        print self.user
        return super(RenkontigxoCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        with transaction.atomic():
            self.arangxo = Arangxo.objects.create(
                    kreanto = self.user,
                    nomo = form.cleaned_data['nomo'],
                    mallonga_nomo = form.cleaned_data['mallonga_nomo'],
                    nb_partoprenantoj = form.cleaned_data['nb_partoprenantoj'],
                    publiko = form.cleaned_data['publiko'],
            )
            self.evento = Evento.objects.create(
                    arangxo = self.arangxo,
                    kreanto = self.user,
                    nb_partoprenantoj = form.cleaned_data['nb_partoprenantoj'],
                    komenco = form.cleaned_data['komenco'],
                    fino = form.cleaned_data['fino'],
                    lat = form.cleaned_data['lat'],
                    long = form.cleaned_data['long'],
                    temo = form.cleaned_data['temo'],
                    urbo = form.cleaned_data['urbo'],
                    posxtkodo = form.cleaned_data['posxtkodo'],
                    lando = form.cleaned_data['lando'],
                    priskribo = form.cleaned_data['priskribo'],
            )
            self.arangxo.etikedoj.add(*form.cleaned_data['etikedoj'])
            return super(RenkontigxoCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('evento_detail', kwargs={'pk': self.evento.pk})

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
        return reverse('arangxo_detail', args=[self.object.id])

arangxo_create = ArangxoCreateView.as_view()


class ArangxoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Arangxo
    form_class = ArangxoForm

    def get_success_url(self):
        return reverse('arangxo_detail', args=[self.object.id])

arangxo_update = ArangxoUpdateView.as_view()


class EventoListView(generic.ListView):
    model = Evento

evento_list = EventoListView.as_view()


class EventoDetailView(generic.DetailView):
    model = Evento

evento_detail = EventoDetailView.as_view()


class EventoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Evento
    form_class = EventoCreateForm

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        self.user = request.user
        return super(EventoCreateView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(EventoCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['arangxo'] = self.pk
        return kwargs

    def get_success_url(self):
        return reverse('evento_detail', args=[self.object.pk])

evento_create = EventoCreateView.as_view()


class EventoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Evento
    form_class = EventoForm

    def get_success_url(self):
        return reverse('evento_detail', args=[self.object.id])

evento_update = EventoUpdateView.as_view()

