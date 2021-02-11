from django.shortcuts import render, redirect
# from .forms import BlogForm

from .models import Post
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import PostForm
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 

def hello(request):
    showall = Post.objects.all()
    return render(request, 'index.htm', {"data": showall})

class HomePageView(ListView):
    showall = Post.objects.all()
    model = Post
    template_name = 'index.htm'

def blogPage(request):
    return render(request, 'blogPage.htm')


def contact_page(request):
    return render(request, 'contact.htm')


def show_blog(request):
    showall = Post.objects.all()
    return render(request, 'blogPage.htm', {"data": showall})


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('title') and request.POST.get('content') and request.POST.get('category'):
            post=Post()
            post.username= request.POST.get('username')
            post.title= request.POST.get('title')
            post.category= request.POST.get('category')
            
            post.content= request.POST.get('content')
            post.save()
                
            return render(request, 'insert-item.htm')  
    else:
        return render(request,'insert-item.htm')

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'insert-item.htm'
    success_url = reverse_lazy('home')