from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        try:
            return super().get_object()
        except:
            raise NotFound("Product not found.")