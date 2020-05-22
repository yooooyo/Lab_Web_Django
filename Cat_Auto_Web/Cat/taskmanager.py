from Cat.models import TestScripts
from Cat.models import Tasktable
from Cat.models import CatInfo

def get_cat_scripts():
    return TestScripts.objects.filter(path__contains='Scripts').values()

def add_scripts(uuts,scripts,tag=None):
    for sn in uuts:
        if tag:
            catinfo_uut = CatInfo.objects.get(sn=sn)
            catinfo_uut.tag = tag
            catinfo_uut.save()
        for script in scripts:
            Tasktable.objects.create(sn=sn,task=script,state='PENDING')
