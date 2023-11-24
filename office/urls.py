from django.urls import path
from . import views 

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
    path('completed_projects', views.completed_projects, name='completed_projects'),
    path('project_details', views.project_details, name='project_details'),
    path('about', views.about, name='about'),
]