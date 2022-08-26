from django.shortcuts import render
from django.http import HttpResponse

# This is a simple view
def index(request):
    return HttpResponse("Hello world, this is a poll site!")
