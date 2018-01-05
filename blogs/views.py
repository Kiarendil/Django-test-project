from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blogs import models

# Create your views here.


class BlogDetail(DetailView):
    template_name = 'blogs/blog_detail.html'
    model = models.Blog


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    model = models.Blog


class PostDetail(DetailView):
    template_name = 'blogs/post_detail.html'
    model = models.Post
