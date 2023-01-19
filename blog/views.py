from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post 

class BlogListView(ListView):
    model = Post 
    context_object_name = 'post_list'
    template_name = 'home.html'

class BlogDetailView(DetailView): 
    model = Post 
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post 
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post 
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')