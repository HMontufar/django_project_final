from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from hobbie.models import Hobbie
from hobbie.forms import HobbieForm


class HobbieListView(ListView):
    model = Hobbie
    paginate_by = 5


class HobbieDetailView(DetailView):
    model = Hobbie
    fields = ["name", "description", "email"]


class HobbieCreateView(LoginRequiredMixin, CreateView):
    model = Hobbie
    success_url = reverse_lazy("hobbie:hobbie-list")

    form_class = HobbieForm

    def form_valid(self, form):
        """Filter to avoid duplicate hobbies"""
        data = form.cleaned_data
        actual_objects = Hobbie.objects.filter(
            name=data["name"],
            description=data["description"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El Pasatiempo {data['name']} ya existe",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Pasatiempo: {data['name']} Creado exitosamente!",
            )
            return super().form_valid(form)


class HobbieUpdateView(LoginRequiredMixin, UpdateView):
    model = Hobbie
    fields = ["name", "description", "email"]

    def get_success_url(self):
        hobbie_id = self.kwargs["pk"]
        return reverse_lazy("hobbie:hobbie-detail", kwargs={"pk": hobbie_id})


class HobbieDeleteView(LoginRequiredMixin, DeleteView):
    model = Hobbie
    success_url = reverse_lazy("hobbie:hobbie-list")
