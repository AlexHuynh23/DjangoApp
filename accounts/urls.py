from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('friends/', views.friends, name='friends'),
    path('likes/', views.likes, name='likes'),
]
