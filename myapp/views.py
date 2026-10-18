from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello, World! This is the home page of my Django application.")

def about(request):
    return HttpResponse("This is the about  page of <H1>my Django application</H1>.")