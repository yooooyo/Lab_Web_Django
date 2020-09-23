from Cat.models import TestScripts
from Cat.models import Tasktable
from Cat.models import CatInfo
from Cat.models import Ap


from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

def get_cat_scripts():
    return TestScripts.objects.filter(path__contains='Scripts').values()

def get_ap_ssid():
    aps = Ap.objects.filter(active=True).values('ssid','ssid_5g')
    aps_list = [list(ap.values()) for ap in aps]
    aps=[]
    for ap in aps_list:
        if ap[0]:
            if not ap[0] in aps:
                aps.append(ap[0])
        if ap[1]:
            if not ap[1] in aps:
                aps.append(ap[1])
    return aps

def add_scripts(uuts,scripts,ap,restart,tag=None):
    for sn in uuts:
        if tag:
            catinfo_uut = CatInfo.objects.get(sn=sn)
            catinfo_uut.tag = tag
            catinfo_uut.ap = ap
            catinfo_uut.save()
        if scripts:
            for script in scripts:
                Tasktable.objects.create(sn=sn,task=script,state='PENDING',ap=ap,need_restart = restart)

def basicfileupload_handle(file):
    with open(f'//lab_server/share/upload/{file.name}','wb+') as d:
        for chunk in file.chunks():
            d.write(chunk) 
