from django.core.urlresolvers import reverse
from django.views import generic

from .forms import (ArangxoForm, EventoCreateForm,  EventoForm,
        EventoArangxoCreateForm)
from .models import Arangxo, Evento


class ArangxoListView(generic.ListView):
    model = Arangxo

arangxo_list = ArangxoListView.as_view()


class ArangxoDetailView(generic.DetailView):
    model = Arangxo

arangxo_detail = ArangxoDetailView.as_view()


class ArangxoCreateView(generic.CreateView):
    model = Arangxo
    form_class = ArangxoForm

    def get_success_url(self):
        return reverse('arangxo_detail', args=[self.object.id])

arangxo_create = ArangxoCreateView.as_view()


class ArangxoUpdateView(generic.UpdateView):
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


class EventoArangxoCreateView(generic.CreateView):
    form_class = EventoArangxoCreateForm
    template_name = 'eventoj/evento_arangxo_form.html'

    def get_success_url(self):
        return reverse('evento_list')

evento_arangxo_create = EventoArangxoCreateView.as_view()


class EventoCreateView(generic.CreateView):
    model = Evento
    form_class = EventoCreateForm

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        return super(EventoCreateView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(EventoCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['arangxo'] = self.pk
        return kwargs

    def get_success_url(self):
        return reverse('evento_detail', args=[self.object.pk])

evento_create = EventoCreateView.as_view()


class EventoUpdateView(generic.UpdateView):
    model = Evento
    form_class = EventoForm

    def get_success_url(self):
        return reverse('evento_detail', args=[self.object.id])

evento_update = EventoUpdateView.as_view()
