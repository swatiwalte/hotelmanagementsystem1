from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('Home', views.Home),
    path('Reception', views.Reception),
    path('Booking', views.Booking),
    path('Gallary', views.Gallary),
    path('Login', views.Login),
    path('register', views.register),
    path('insert', views.insert),
    path('logintask', views.logintask),
    path('signout', views.signout),
    path('About', views.About),
    path('Help', views.Help),
    
]