from django.core.urlresolvers import reverse
from django.views import generic

from braces.views import LoginRequiredMixin

from .forms import OrganizoForm
from .models import Organizo


class OrganizoListView(generic.ListView):
    model = Organizo

organizo_list = OrganizoListView.as_view()


class OrganizoDetailView(generic.DetailView):
    model = Organizo

organizo_detail = OrganizoDetailView.as_view()


class OrganizoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Organizo
    form_class = OrganizoForm

    def get_success_url(self):
        return reverse('organizo_detail', args=[self.object.id])

organizo_create = OrganizoCreateView.as_view()


class OrganizoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Organizo
    form_class = OrganizoForm

    def get_success_url(self):
        return reverse('organizo_detail', args=[self.object.id])

organizo_update = OrganizoUpdateView.as_view()
