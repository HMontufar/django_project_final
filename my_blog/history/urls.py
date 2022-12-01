from django.urls import path

from history import views

app_name = "history"
urlpatterns = [
    path("historys/", views.HistoryListView.as_view(), name="history-list"),
    path("history/add/", views.HistoryCreateView.as_view(), name="history-add"),
    path("history/<int:pk>/detail/", views.HistoryDetailView.as_view(), name="history-detail"),
    path("history/<int:pk>/update/", views.HistoryUpdateView.as_view(), name="history-update"),
    path("history/<int:pk>/delete/", views.HistoryDeleteView.as_view(), name="history-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
