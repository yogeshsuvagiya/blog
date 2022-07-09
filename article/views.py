

from django.shortcuts import render


def homepage(request):
    return render(request,"home.html",{})

def services(request):
    return render(request,"services.html",{})

def aboutUs(request):
    return render (request,'about.html',{})