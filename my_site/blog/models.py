from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150)
    upload_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)
    short_inf = models.CharField(max_length=150)

class body(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    created_at = models.DateField(auto_now=True)