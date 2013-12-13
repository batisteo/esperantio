from django.views import generic
from django.shortcuts import render

from .models import Evento


class EventoDetailView(generic.DetailView):
    model = Evento

evento_detail = EventoDetailView.as_view()


class EventoCreateView(generic.CreateView):
    model = Evento

evento_create = EventoCreateView.as_view()
