from django.urls import path

from hobbie import views

app_name = "hobbie"
urlpatterns = [
    path("hobbies", views.HobbieListView.as_view(), name="hobbie-list"),
    path("hobbie/add/", views.HobbieCreateView.as_view(), name="hobbie-add"),
    path("hobbie/<int:pk>/detail/", views.HobbieDetailView.as_view(), name="hobbie-detail"),
    path("hobbie/<int:pk>/update/", views.HobbieUpdateView.as_view(), name="hobbie-update"),
    path("hobbie/<int:pk>/delete/", views.HobbieDeleteView.as_view(), name="hobbie-delete"),
]
