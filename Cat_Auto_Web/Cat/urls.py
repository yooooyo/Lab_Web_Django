from Cat import views
from django.urls import path, include

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("taskmanager/", views.taskmanager, name="taskmanager"),
    path("about/", views.about, name="about"),
]
