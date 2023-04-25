from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, ahmed khlif. You're at the polls index.")