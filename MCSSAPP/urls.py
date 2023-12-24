from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('administration', views.administration, name='administration'),
    path('news', views.news, name='news'),
    path('<int:pk>/', views.newsdetails, name='newsdetails'),
    path('seniormanagement/<int:image_id>', views.seniormanagement),

]