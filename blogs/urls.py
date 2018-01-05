from django.conf.urls import url

from blogs import views

urlpatterns = [
    url(r'^$', views.BlogList.as_view(), name='blog_list'),
    url(r'^blog/(?P<pk>\d+)', views.BlogDetail.as_view(), name='blog'),
    url(r'^blog/posts/(?P<pk>\d+)', views.PostDetail.as_view(), name='post'),
]