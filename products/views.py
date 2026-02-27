from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_object(self):
        try:
            return super().get_object()
        except:
            raise NotFound(detail="Product not found.")