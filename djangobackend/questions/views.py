from django.http import JsonResponse
from . import service


def index(request):
    return JsonResponse(service.get_questions(), safe=False)
