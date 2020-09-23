from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Cat import testresult as t_result
from Cat import dashboard as d_board
from Cat import taskmanager as t_mgr
from os import listdir
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


file = listdir('//lab_server/share/upload')
def taskmanager(request):
    sn_list = request.POST.getlist('selected_sn',)
    if 'delete-uut' in request.POST:
        if sn_list:
            d_board.delete_uut(sn_list)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    elif 'add-task' in request.POST:
        if sn_list:
            scripts = t_mgr.get_cat_scripts()
            aps = t_mgr.get_ap_ssid()
            pvt = [script['name'] for script in scripts if script['tool']=='winpvt']
            pws = [script['name'] for script in scripts if script['tool']=='powerstress']
            wwan = [script['name'] for script in scripts if script['wwan']]
            wlan = [script['name'] for script in scripts if script['wlan']]
            lan = [script['name'] for script in scripts if script['lan']]
            files = file
            data={
                'sn_list':sn_list,
                'pvt':pvt,
                'pws':pws,
                'wwan':wwan,
                'wlan':wlan,
                'lan':lan,
                'aps':aps,
                'files':files
            }
            return render(request, 'Cat/taskmanager.html',data)

def task_delete(request):
    task_ids = request.POST.getlist('select_taskid')
    t_result.delete_task(task_ids)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def ajax_taskAdd(request):
    if request.is_ajax():
        uuts = request.POST.getlist('sn[]')
        scripts = request.POST.getlist('scripts[]')
        tag = request.POST.get('tag')
        ap = request.POST.get('ap')
        driver = request.POST.get('driver')
        restart = request.POST.get('restart')
        if driver:
            scripts = [driver]
        t_mgr.add_scripts(uuts,scripts,ap,restart,tag)
        return render(request,'Cat/taskmanager.html')

def fileupload(request):
    form =  t_mgr.UploadFileForm()
    if request.method == 'POST':
        form =  t_mgr.UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            t_mgr.basicfileupload_handle(request.FILES['file'])
            return HttpResponse('File Upload Success !!!')
        else:
            form = t_mgr.UploadFileForm()
    return render(request,'Cat/fileupload.html',{'uploadform':form})

def about(request):
    return render(request, 'Cat/about.html')

