from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import BlogPage

def home(request):
    template = loader.get_template('index.html')
    lstBlogPage = BlogPage.objects.all()
    data = {
        'prenom': 'Rayan',
        'blogpages': lstBlogPage
    }
    return HttpResponse(template.render(data, request))


