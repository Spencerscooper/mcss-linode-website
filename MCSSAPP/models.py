
from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime 

class Post(models.Model):
    heading = models.CharField(max_length=100)
    date_release = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploaded/galleries', blank=True, null=True)
    body = models.TextField()
    
    class Meta:
        ordering = ('-heading',)

class Senior_Management_Image(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=40)
    image = models.ImageField(upload_to='uploadedimages', blank=True, null=True)

    def __str__(self):
        return self.name

   

