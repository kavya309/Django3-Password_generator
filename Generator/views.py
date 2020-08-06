from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request,'Generator/home.html')
def about(request):
    return render(request,'Generator/about.html')
def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#%^&*()')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    length=int(request.GET.get('length',12))
    thepassword=''
    password=0
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'Generator/password.html',{'password':thepassword})