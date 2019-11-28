

# Create your views here.
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def doctor(request):
    return render(request,'doctor.html')

def elements(request):
    return render(request,'elements.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def singleblog(request):
    return render(request,'single-blog.html')

# Python program to view
# for displaying images

