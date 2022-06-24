from django.db import models

class Post(models.Model):
    section_select = models.CharField(max_length=80)
    section_select2 = models.CharField(max_length=80)
    section_select3 = models.CharField(max_length=80)
    section_menu =  models.CharField(max_length=100)
    section_menu2 =  models.CharField(max_length=100)
    section_menu3 =  models.CharField(max_length=100)
    section_menu4 =  models.CharField(max_length=100)
    section_menu5 =  models.CharField(max_length=100)
    filter = models.CharField(max_length=30)


class Post_all(models.Model):
    title = models.CharField(max_length=50)
    account_name = models.CharField(max_length=60)
    likes = models.IntegerField()
    view = models.IntegerField()

