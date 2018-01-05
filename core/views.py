from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import DetailView, ListView

from core import models

# Create your views here.


def index(reqest):

    return render(reqest, 'core/base.html')

