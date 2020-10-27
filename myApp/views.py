from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import urlparse

# Create your views here.

def index(request):
    # print(request.build_absolute_uri)
    # print(request.path)
    # print(request.get_full_path)
    print("hellow")
    print(request.META['HTTP_HOST'])
    url = request.META['HTTP_HOST']
    x = url.split(".")
    return HttpResponse(x[0])