from django.shortcuts import render, HttpResponse


# Create your views here.
def say_say_hello(request):
    return HttpResponse("Hello")
