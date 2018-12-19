from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.



def index(request):
    posts = Posts.objects.all()[:10]
    template_data = {
        'title':'Latest Posts',
        'posts':posts
    }
    return render(request, 'posts/index.html', template_data)

def details(request, id):
    post = Posts.objects.get(id=id)
    template_data = {
        'post':post
    } 
    return render(request, 'posts/details.html', template_data)

