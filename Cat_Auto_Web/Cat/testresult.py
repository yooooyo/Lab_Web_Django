from Cat.models import Testlogtable
from Cat.models import Tasktable
from Cat.models import Loglisttable
from django.shortcuts import render
from django.http import HttpResponse


def capturelog(sn):
    tasks = list(Tasktable.objects.filter(sn=sn).values())
    testlogs = list(Testlogtable.objects.filter(sn=sn).values())
    loglists_blacklist_ids = [ id['id'] for id in Loglisttable.objects.filter(blacklist=True).values('id')]
    logs = [testlog for task in tasks for testlog in testlogs if testlog['taskid'] == task['id'] and (testlog['loglistid'] in loglists_blacklist_ids)]
    
    tasks_logs = []

    for task in tasks:
        if task not in tasks_logs:
            tasks_logs.append((task,[log for log in logs if log['taskid']== task['id']]))

    return tasks_logs



