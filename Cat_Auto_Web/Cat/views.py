from django.shortcuts import render
from django.http import HttpResponse
from Cat import testresult as t_result
from Cat import dashboard as d_board
from Cat import taskmanager as t_mgr
# Create your views here.

def dashboard(request):
    search =  {'platform':'','tag':'','sn':''}
    if request.method == 'GET':
        search['platform'] = request.GET.get('platform')
        search['tag'] = request.GET.get('tag')
        search['sn'] = request.GET.get('sn')      
        uut_list = d_board.list_uut(**search)
    else:
        uut_list = d_board.list_uut()
    return render(request,'Cat/dashboard.html',{'uut_list':uut_list})

def testresult(request,sn):
    tasks_logs = t_result.capturelog(sn)
    return render(request, 'Cat/testresult.html',{'tasks_logs':tasks_logs})

def taskmanager(request):
    sn_list = request.POST.getlist('selected_sn',)
    if sn_list:
        scripts = t_mgr.get_cat_scripts()
        pvt = [script['name'] for script in scripts if script['tool']=='winpvt']
        pws = [script['name'] for script in scripts if script['tool']=='powerstress']
        wwan = [script['name'] for script in scripts if script['wwan']]
        wlan = [script['name'] for script in scripts if script['wlan']]
        lan = [script['name'] for script in scripts if script['lan']]
        data={
            'sn_list':sn_list,
            'pvt':pvt,
            'pws':pws,
            'wwan':wwan,
            'wlan':wlan,
            'lan':lan,
        }
        return render(request, 'Cat/taskmanager.html',data)

def ajax_submit(request):
    if request.method == 'POST':
        print(request.POST) 
    return render(request,'Cat/ajax_submit.html') 

def ajax_taskAdd(request):
    if request.is_ajax():
        uuts = request.POST.getlist('sn[]')
        scripts = request.POST.getlist('scripts[]')
        tag = request.POST.get('tag')
        t_mgr.add_scripts(uuts,scripts,tag)
        return render(request,'Cat/taskmanager.html')

def about(request):
    return render(request, 'Cat/about.html')

