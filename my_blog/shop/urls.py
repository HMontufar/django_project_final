from django.urls import path

from shop import views

app_name = "shop"
urlpatterns = [
    path("shops", views.ShopListView.as_view(), name="shop-list"),
    path("shop/add/", views.ShopCreateView.as_view(), name="shop-add"),
    path("shop/<int:pk>/detail/", views.ShopDetailView.as_view(), name="shop-detail"),
    path("shop/<int:pk>/update/", views.ShopUpdateView.as_view(), name="shop-update"),
    path("shop/<int:pk>/delete/", views.ShopDeleteView.as_view(), name="shop-delete"),
]
