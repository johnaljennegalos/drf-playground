from certifi import contents
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)

        title = serializer.validated_data['title']
        content = serializer.validated_data['content'] or None

        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer