from django.shortcuts import render
from django.http import HttpResponse
from Cat.models import CatInfo

# Create your views here.

# def dashboard(request):
#     return render(request,'Cat/dashboard.html')



def taskmanager(request):
    return render(request, 'Cat/taskmanager.html')

def about(request):
    return render(request, 'Cat/about.html')
