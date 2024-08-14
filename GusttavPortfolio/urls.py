# we import here django.urls and path to create the url that we are gonna see in the web
from django.urls import path

# here we are imported all that views have
from . import views

urlpatterns = [
    # here we are creating the path the its gonna execute the rute to the coresponding url 
    path('', views.home),
    path('about_me/', views.about_me),
    path('resume/', views.resume),
    path('contac/', views.contac),
]