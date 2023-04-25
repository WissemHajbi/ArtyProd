from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, ahmed. You're at the polls index.")