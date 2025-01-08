from .models import BlogPage
from .models import BlogPage, BlogPageAdmin
from django.contrib import admin

# Register your models here.
admin.site.register(BlogPage, BlogPageAdmin)
