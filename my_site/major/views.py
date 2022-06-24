from django.shortcuts import render
from .models import Post, Post_all

def index(request):
    p = Post.objects.all()

    return render(request, 'major/index.html', {
        "post": p
    })

def all(req):
    a = Post_all.objects.all()

    return render(req, 'major/all.html', {
        "all": a
    })

def animation(req):
    a = Post_all.objects.all()

    return render(req, 'major/animation.html', {
        "all": a
    })

def print(req):
    a = Post_all.objects.all()

    return render(req, 'major/print.html', {
        "all": a
    })

def brand(req):
    a = Post_all.objects.all()

    return render(req, 'major/brand.html', {
        "all": a
    })

def mobile(req):
    a = Post_all.objects.all()

    return render(req, 'major/mobile.html', {
        "all": a
    })