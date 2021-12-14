from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponseRedirect(reverse('polls:index'))

