from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from main.services import parse


def time(request):
    test = parse()
    return JsonResponse(test, safe=False)  # TODO: Safe or not ???
