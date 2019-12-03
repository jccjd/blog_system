from django.contrib import admin

from .models import Blog,Tag,Catagory
# Register your models here.
admin.site.register([Blog, Tag, Catagory])