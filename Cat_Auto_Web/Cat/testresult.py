from Cat.models import Testlogtable
from Cat.models import Tasktable
from Cat.models import Loglisttable
from django.shortcuts import render
from django.http import HttpResponse

def capturelog(sn):
    return Tasktable.object.filter(sn=sn)

def testresult(request,sn):
    capturelog(sn)
    return render(request, 'Cat/testresult.html')