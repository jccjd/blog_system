from django.db import models


# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=30)


class Tag(models.Model):
    name = models.CharField(max_length=16)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE,verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, models.CASCADE, verbose_name='博客')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.CharField('内容', max_length=200)
    created = models.DateTimeField(auto_now_add=True)
