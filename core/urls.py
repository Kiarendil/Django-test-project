from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/base.html'), name='index'),
    url(r'^index/$', TemplateView.as_view(template_name='core/base.html')),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/$', logout, {'template_name': 'core/logout.html'}, name="logout"),
]
