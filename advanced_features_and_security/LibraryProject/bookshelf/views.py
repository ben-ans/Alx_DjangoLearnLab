from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to the bookshelf")

def hello(request, first_name):
    return HttpResponse(f"You are welcom {first_name}")