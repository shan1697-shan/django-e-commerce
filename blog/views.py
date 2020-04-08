
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blogpost

def index(request):
    allblog = Blogpost.objects.all()
    n = len(allblog)
    dict= {'allblog':allblog, 'length':n}
    return render(request, 'blog/index.html',dict)

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogpost.html', {'post':post})