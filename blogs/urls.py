from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^question/(?P<pk>\d+)', views.QuestionDetail.as_view()),
    url(r'^test/(?P<name>\d+)', views.helloworld),
    url(r'^html/(?P<name>\d+)', views.htmlhello),
]