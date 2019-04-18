from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def indexBlog(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', {'posts':posts})
