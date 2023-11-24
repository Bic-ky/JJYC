from django.shortcuts import render
from .models import Projects


def contact(request):
    return render(request, 'office/contact.html')


def projects(request):
    return render(request, 'office/projects.html')

def completed_projects(request):
    return render(request, 'office/completed_projects.html')


def project_details(request):
    return render(request, 'office/project_details.html')

def about(request):
    return render(request, 'office/about.html')