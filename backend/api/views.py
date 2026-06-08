import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductsSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Products.objects.all().order_by("?").first()
    data = {}

    if instance:
        #data = model_to_dict(model_data)
        #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductsSerializer(instance).data
    return Response(data)
