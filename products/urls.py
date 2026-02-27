from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

from django.urls import path
from .views_ui import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls


urlpatterns += [
    path("ui/products/", ProductListView.as_view(), name="product_list"),
    path("ui/products/create/", ProductCreateView.as_view(), name="product_create"),
    path("ui/products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("ui/products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]