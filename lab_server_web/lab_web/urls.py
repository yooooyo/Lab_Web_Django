from django.urls import path
from lab_web import views
from lab_web.models import CatInfo

home_list_view = views.UUTListView.as_view(
    queryset=CatInfo.objects.all(),  # :5 limits the results to the five most recent
    context_object_name = 'uut_list',
    template_name = 'lab_web/dashboard.html'
)

urlpatterns = [
    path("",home_list_view,name='dashboard'),
    path("taskmanager/",views.taskmanager,name='taskmanager')
]