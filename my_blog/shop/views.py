from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from shop.models import Shop
from shop.forms import ShopForm


class ShopListView(ListView):
    model = Shop
    paginate_by = 5


class ShopDetailView(DetailView):
    model = Shop
    fields = ["name", "modelo", "email", "collection"]


class ShopCreateView(LoginRequiredMixin, CreateView):
    model = Shop
    success_url = reverse_lazy("shop:shop-list")

    form_class = ShopForm

    def form_valid(self, form):
        """Filter to avoid duplicate shops"""
        data = form.cleaned_data
        actual_objects = Shop.objects.filter(
            name=data["name"],
            modelo=data["modelo"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El Producto {data['name']} - {data['modelo']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Producto: {data['name']} Creado exitosamente!",
            )
            return super().form_valid(form)


class ShopUpdateView(LoginRequiredMixin, UpdateView):
    model = Shop
    fields = ["name", "modelo", "email", "collection"]

    def get_success_url(self):
        shop_id = self.kwargs["pk"]
        return reverse_lazy("shop:shop-detail", kwargs={"pk": shop_id})


class ShopDeleteView(LoginRequiredMixin, DeleteView):
    model = Shop
    success_url = reverse_lazy("shop:shop-list")