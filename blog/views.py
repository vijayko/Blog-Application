from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'body']
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 
