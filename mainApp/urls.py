from django.urls import path
from . import views 
from .views import ProjectListView 

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('completed_projects', views.completed_projects, name='completed_projects'),
    path('project_details', views.project_details, name='project_details'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('announcement/', views.announcement, name='announcement'),
]