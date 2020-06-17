from Cat.models import Testlogtable
from Cat.models import Tasktable
from Cat.models import Loglisttable
from django.shortcuts import render
from django.http import HttpResponse
import re

def delete_task(ids):
    if ids:
        for id in ids:
            Tasktable.objects.get(id=id).delete()

def capturelog(sn):
    tasks = list(Tasktable.objects.filter(sn=sn).values())
    testlogs = list(Testlogtable.objects.filter(sn=sn).values())
    loglists_blacklist_ids = [ id['id'] for id in Loglisttable.objects.filter(blacklist=True).values('id')]
    logs = [testlog for task in tasks for testlog in testlogs if testlog['taskid'] == task['id'] and (testlog['loglistid'] in loglists_blacklist_ids)]
    
    tasks_logs = []

    for task in tasks:
        if task not in tasks_logs:
            tasks_logs.append((task,[log for log in logs if log['taskid']== task['id']]))

    for task,logs in tasks_logs:
        if task['state'] == 'DONE':
            result = task['result']
            if not task['result']:
                for log in logs:
                    result = log['detail']
                    if not result:
                        task['summary'] = 'pass'
                    else:
                        task['summary'] = 'error'
            else:
                if result.find('Errors')>0:
                    task['summary'] = 'error'
                elif result.find('Warning')>0:
                    task['summary'] = 'warning'
                else:
                    task['summary'] = 'pass'

    return tasks_logs[::-1]



