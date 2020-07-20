from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is working now")

# Create your views here.
