from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.urls import reverse_lazy
from django.urls import reverse 

from .models import Post, Comment
from .forms import CommentForm

class BlogListView(ListView):
    model = Post 
    context_object_name = 'post_list'
    template_name = 'home.html'

class BlogDetailView(LoginRequiredMixin, FormMixin, DetailView): 
    model = Post 
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail_view', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context 
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else: 
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BlogDetailView, self).form_valid(form)


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
