from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Senior_Management_Image



# Create your views here.

def index(request):
    return render(request,'MCSSAPP/index.html')

def about(request):
    return render(request, 'MCSSAPP/about.html')

def administration(request):
    return render(request, 'MCSSAPP/administration.html')

def news(request):
    news = Post.objects.all()
    return render(request, 'MCSSAPP/news.html',{"news":news})


def newsdetails(request, pk):

    return render(request,'MCSSAPP/newsdetails.html')


def seniormanagement(request, image_id):
    seniormanagement = Senior_Management_Image.objects.all(pk=image_id)
    if seniormanagement is not None:
        return render(request, 'MCSSAPP/index.html', {'seniormanagementteam':seniormanagement})
