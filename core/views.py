from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import DetailView

from core import models

# Create your views here.


def index(reqest):

    return render(reqest, 'core/base.html')


def helloworld(reqest, name=None):

    return HttpResponse('Hello world! <br> This page number ' + name + ' is working.')


def htmlhello(reqest, name=None):

    return render(reqest, 'core/base.html', {'name': name})


class QuestionDetail(DetailView):
    template_name = 'core/question_detail.html'
    model = models.Question


def question_detail(reqest, pk=None):
    question = get_object_or_404(models.Question.objects.all(), pk=pk)
    return render(reqest, 'core/question_detail.html', {'question': question, })
