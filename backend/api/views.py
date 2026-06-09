import json
from django.forms.models import model_to_dict
from rest_framework import status
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductsSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"message": "Invalid data"}, status=400)
