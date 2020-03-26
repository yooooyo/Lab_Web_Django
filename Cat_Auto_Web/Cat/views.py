from django.shortcuts import render
from django.http import HttpResponse
from Cat.models import CatInfo
from django.views.generic import ListView
# Create your views here.



class UUTListView(ListView):
    model = CatInfo
    def get_context_data(self,**kwargs):
        context = super(UUTListView,self).get_context_data(**kwargs)
        return context

def dashboard(request):
    return render(request,'Cat/dashboard.html')

def taskmanager(request):
    return render(request, 'Cat/taskmanager.html')

def about(request):
    return render(request, 'Cat/about.html')
