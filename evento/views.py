from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import Evento


class EventoListView(generic.ListView):
    model = Evento

evento_list = EventoListView.as_view()


class EventoDetailView(generic.DetailView):
    model = Evento

evento_detail = EventoDetailView.as_view()


class EventoCreateView(generic.CreateView):
    model = Evento
    
    def get_success_url(self):
        return reverse('evento_detail', args=[self.object.id])

evento_create = EventoCreateView.as_view()


class EventoUpdateView(generic.UpdateView):
    model = Evento
    
    def get_success_url(self):
        return reverse('evento_detail', args=[self.object.id])

evento_update = EventoUpdateView.as_view()
