from django.http import JsonResponse
from django.shortcuts import render
from . import service


def index(request):
    return JsonResponse(service.get_social_media_post())
