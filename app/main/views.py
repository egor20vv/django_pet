from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1><b>Index</b></h1>')


def polls(request):
    return HttpResponse('<h1><b>Polls</b></h1>')
