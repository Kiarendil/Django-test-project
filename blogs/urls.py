from django.conf.urls import url

import core.views
from blogs import views

urlpatterns = [
    url(r'^$', views.BlogList.as_view(), name='blog_list'),
    url(r'^blog/(?P<pk>\d+)', views.BlogDetail.as_view(), name='blog'),
    url(r'^blog/posts/(?P<pk>\d+)', views.PostDetail.as_view(), name='post'),
    url(r'^question/$', core.views.QuestionList.as_view(), name='question_list'),
    url(r'^question/(?P<pk>\d+)', core.views.QuestionDetail.as_view(), name='question'),
    url(r'^test/(?P<name>\d+)', core.views.helloworld),
    url(r'^html/(?P<name>\d+)', core.views.htmlhello),
]