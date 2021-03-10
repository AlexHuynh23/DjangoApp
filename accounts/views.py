from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Account Home Page")

def friends(request):
    return HttpResponse("Account friends Page")

def likes(request):
    return HttpResponse("Account Liked Page")
