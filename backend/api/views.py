from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({'message': 'Hello John, this is your first Django API response!'})
