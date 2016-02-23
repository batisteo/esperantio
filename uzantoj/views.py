from django.conf import settings
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm

from braces.views import LoginRequiredMixin

from .models import Uzanto
from .forms import CustomUserChangeForm, UzantoCreateForm


class UzantoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Uzanto

    def get_object(self):
        return self.request.user

uzanto_detail = UzantoDetailView.as_view()


class UzantoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Uzanto
    form_class = CustomUserChangeForm

    def get_object(self):
        return self.request.user

uzanto_update = UzantoUpdateView.as_view()


class UzantoCreateView(generic.CreateView):
    model = Uzanto
    form_class = UzantoCreateForm
    success_url = settings.LOGIN_REDIRECT_URL

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UzantoCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form, *args, **kwargs):
        form_valid = super(UzantoCreateView, self).form_valid(form, *args, **kwargs)
        login(self.request, self.object)
        return form_valid

uzanto_create = UzantoCreateView.as_view()


class PasswordChangeView(LoginRequiredMixin, generic.FormView):
    model = Uzanto
    form_class = PasswordChangeForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'uzantoj/password_form.html'

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

password_change = PasswordChangeView.as_view()
