from Cat import views
from django.urls import path, include
from Cat import dashboard



urlpatterns = [
    path("", dashboard.dashboard_uut_list, name="dashboard"),
    path("testresult/<sn>", views.testresult, name="testresult"),
    path("taskmanager/", views.taskmanager, name="taskmanager"),
    path("about/", views.about, name="about"),
]
