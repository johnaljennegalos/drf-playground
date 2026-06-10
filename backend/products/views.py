from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer