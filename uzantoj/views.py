from django.views import generic
from django.contrib.auth import login

from .models import Uzanto
from .forms import CustomUserChangeForm, UzantoCreateForm


class UzantoDetailView(generic.DetailView):
    model = Uzanto
    
    def get_object (self):
        return self.request.user

uzanto_detail = UzantoDetailView.as_view()


class UzantoUpdateView(generic.UpdateView):
    model = Uzanto
    form_class = CustomUserChangeForm
    
    def get_object (self):
        return self.request.user

uzanto_update = UzantoUpdateView.as_view()


class UzantoCreateView(generic.CreateView):
    model = Uzanto
    form_class = UzantoCreateForm
    
    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UzantoCreateView, self).get(request, *args, **kwargs)
    
    def form_valid(self, form, *args, **kwargs):
        form_valid = super(UzantoCreateView, self).form_valid(form, *args, **kwargs)
        login(self.request, self.object)
        return form_valid

uzanto_create = UzantoCreateView.as_view()
