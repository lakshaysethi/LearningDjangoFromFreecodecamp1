from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(r,*args,**kargs):
    print(r.user ,"just came here to home" )
   # return HttpResponse('<h1>from http response hello world</h1>')
    return render(r, 'pages/home.html', {'title': 'home'})


def contact_view(r,*args,**kargs):
    return render(r, 'pages/contact.html', {'title': 'contact'})

def about_view(r,*args,**kargs):
    return render(r, 'pages/about.html', {'title': 'about'})