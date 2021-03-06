from django.urls import path, include
from Cat import views



urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("testresult/<sn>", views.testresult, name="testresult"),
    path("taskmanager/", views.taskmanager, name="taskmanager"),
    path("about/", views.about, name="about"),
    path("ajax_taskAdd/", views.ajax_taskAdd, name="ajax_taskAdd"),
    path("task_delete/", views.task_delete, name="task_delete"),
    path("fileupload/", views.fileupload, name="fileupload"),
]
