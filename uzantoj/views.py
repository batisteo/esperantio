from django.views import generic

from .models import Uzanto
from .forms import CustomUserChangeForm


class UzantoDetailView(generic.DetailView):
    model = Uzanto
    
    def get_object (self):
        return self.request.user

uzanto_detail = UzantoDetailView.as_view()


class UzantoUpdateView(generic.UpdateView):
    model = Uzanto
    form = CustomUserChangeForm
    
    def get_object (self):
        return self.request.user

uzanto_update = UzantoUpdateView.as_view()
