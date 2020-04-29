from django.shortcuts import render
from django.http import HttpResponse
from Cat import testresult as t_result
from Cat import dashboard as d_board
# Create your views here.

def dashboard(request):
    uut_list = d_board.list_uut()
    return render(request,'Cat/dashboard.html',{'uut_list':uut_list})

def testresult(request,sn):
    tasks_logs = t_result.capturelog(sn)
    return render(request, 'Cat/testresult.html',{'tasks_logs':tasks_logs})

def taskmanager(request):
    return render(request, 'Cat/taskmanager.html')

def about(request):
    return render(request, 'Cat/about.html')
