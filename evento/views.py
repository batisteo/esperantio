from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils import simplejson
from django.views import generic
from django.views.generic.detail import BaseDetailView, \
    SingleObjectTemplateResponseMixin

from .forms import ArangxoForm, EventoCreateForm,  EventoForm
from .models import Arangxo, Evento


class JSONResponseMixin(object):
    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))
    def get_json_response(self, content, **httpresponse_kwargs):
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)
    def convert_context_to_json(self, context):
        return simplejson.dumps(context)


class HybridDetailView(JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView):
    def render_to_response(self, context):
        if self.request.is_ajax():
            obj = context['object'].as_dict()
            return JSONResponseMixin.render_to_response(self, obj)
        else:
            return SingleObjectTemplateResponseMixin.render_to_response(self, context)


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
        return reverse('evento_detail', args=[self.object.id])

evento_create = EventoCreateView.as_view()


class EventoUpdateView(generic.UpdateView):
    model = Evento
    form_class = EventoForm
    
    def get_success_url(self):
        return reverse('evento_detail', args=[self.object.id])

evento_update = EventoUpdateView.as_view()
