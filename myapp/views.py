from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<H1>Hello, World! This is the home page of my Django application.</H1>")

def about(request):
    return HttpResponse("<H2>This is the about  page of my Django application</H2>.")