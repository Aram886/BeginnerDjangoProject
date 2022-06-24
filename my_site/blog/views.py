from django.shortcuts import render
from .models import Article,body

def blog(r):
    b = Article.objects.all()
    bod = body.objects.all()

    return render(r, 'blog/blog.html', {
        'blog': b,
        'body': bod
    })
