from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))
    thepassword = ''.join(random.choices(characters,k=length))
    return render(request,'generator/password.html',{'password' : thepassword})


def about(request):
    return render(request,'generator/about.html')
