from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def helloworld(reqest, name=None):

    return HttpResponse('Hello world! <br> This page number ' + name + ' is working.')


def htmlhello(reqest, name=None):

    return render(reqest, 'base.html', {'name': name})
