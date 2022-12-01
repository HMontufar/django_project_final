from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from history.forms import CommentForm
from history.forms import HistoryForm

from history.models import Comment
from history.models import History



class HistoryListView(ListView):
    model = History
    paginate_by = 3


class HistoryDetailView(DetailView):
    model = History
    template_name = "history/history_detail.html"
    fields = ["name", "code", "description"]

    def get(self, request, pk):
        history = History.objects.get(id=pk)
        comments = Comment.objects.filter(history=history).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "history": history,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class HistoryCreateView(LoginRequiredMixin, CreateView):
    model = History
    success_url = reverse_lazy("history:history-list")

    form_class = HistoryForm
    # fields = ["name", "code", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate historys"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = History.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La historia {data['name']} - {data['code']} ya existe, crea una nueva",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Historia {data['name']} - {data['code']} creada exitosamente!",
            )
            return super().form_valid(form)


class HistoryUpdateView(LoginRequiredMixin, UpdateView):
    model = History
    fields = ["name", "code", "description", "image"]

    def get_success_url(self):
        history_id = self.kwargs["pk"]
        return reverse_lazy("history:history-detail", kwargs={"pk": history_id})


class HistoryDeleteView(LoginRequiredMixin, DeleteView):
    model = History
    success_url = reverse_lazy("history:history-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        history = get_object_or_404(History, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, history=history
        )
        comment.save()
        return redirect(reverse("history:history-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        history = self.object.history
        return reverse("history:history-detail", kwargs={"pk": history.id})
