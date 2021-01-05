from django.shortcuts import render
from django.http import HttpResponse
import markdown2

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")