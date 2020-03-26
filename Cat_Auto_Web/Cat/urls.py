from Cat import views
from Cat.models import CatInfo
from django.urls import path, include

dashboard_uut_list = views.UUTListView.as_view(
    queryset=CatInfo.objects.order_by('-lastusedtime'),
    context_object_name='uut_list',
    template_name='Cat/dashboard.html',
)

urlpatterns = [
    path("", dashboard_uut_list, name="dashboard"),
    path("taskmanager/", views.taskmanager, name="taskmanager"),
    path("about/", views.about, name="about"),
]
