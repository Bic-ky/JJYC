from django.urls import path
from . import views 
from .views import completed_projects,project_details,projects

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
    path('completed_projects/', completed_projects, name='completed_projects'),
    path('project/<int:project_id>/', project_details, name='project_details'),

]