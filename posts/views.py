# from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView): 
    """
    PostListView is going to retrieve all of the objects from the Post table in the database
    """
    template_name = "posts/list.html"
    model = Post
    context_object_name = "post"


class PostDetailView(DetailView): 
    """
    PostDetailView is going to retrieve a single element from the Post table in the db.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"


class PostCreateView(CreateView): # POST
    """
    PostCreateView is going to allow us to create a new post an add it to the db
    """
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        print(User.objects.all())
        form.instance.author = User.objects.last() 
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    """
    PostUpdateView allows us to update an existing post from the db
    """
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle","body"]

class PostDeleteView(DeleteView):
    """
    PostDeleteView allows us to delete an existing post from the db
    """

    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")