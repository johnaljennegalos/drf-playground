from certifi import contents
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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

class ProductListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)

        title = serializer.validated_data['title']
        content = serializer.validated_data['content'] or None

        if content is None:
            content = title
        serializer.save(content=content)

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        #detail view
        if pk is not None:
            obj = get_object_or_404(Products, pk=pk)
            data  = ProductsSerializer(obj, many=False).data
            return Response(data)


        #list view
        queryset = Products.objects.all()
        data = ProductsSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data['title']
            content = serializer.validated_data['content'] or None

            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"message": "Invalid data"}, status=400)