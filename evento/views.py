from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render

from .models import Evento

class EventoDetailView(DetailView):
    model = Evento

evento_detail = EventoDetailView.as_view()
