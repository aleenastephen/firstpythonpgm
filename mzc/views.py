from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexpage(request):
    return HttpResponse("Welcome to My Index Page")
def contactpage(request):
    return HttpResponse("Contact Page")  
def homepage(request):
    return HttpResponse("Welcome to My Home Page")      

