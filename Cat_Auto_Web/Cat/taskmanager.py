from Cat.models import TestScripts
from Cat.models import Tasktable

def get_cat_scripts():
    return TestScripts.objects.filter(path__contains='Scripts').values()

def add_scripts(uuts,scripts):
    for sn in uuts:
        for script in scripts:
            Tasktable.objects.create(sn=sn,task=script,state='PENDING')
