from django.views.generic import ListView
from django.shortcuts import render
from django.db import connections  
from lab_web.models import CatInfo

# Create your views here.
class UUTListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = CatInfo

    def get_context_data(self, **kwargs):
        # curs = connections['default'].cursor()  
        # curs = curs.execute("select * from cat_info") 
        # curs = curs.fetchall()
        # for row in curs:
        #     print(row) 
        # print(curs)
        context = super(UUTListView, self).get_context_data(**kwargs)
        return context

# def dashboard(request):
#     return render(request,'lab_web/dashboard.html')

def taskmanager(request):
        return render(request, 'lab_web/taskmanager.html')
