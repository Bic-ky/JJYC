from django.shortcuts import render, get_object_or_404
from .models import Projects

def contact(request):
    return render(request, 'office/contact.html')

def projects(request):
    ongoing_projects = Projects.objects.filter(status='ongoing')
    return render(request, 'office/projects.html', {'projects': ongoing_projects})

def about(request):
    return render(request, 'office/about.html')

def completed_projects(request):
    completed_projects = Projects.objects.filter(status='completed')
    return render(request, 'office/completed_projects.html', {'projects': completed_projects})

def project_details(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    return render(request, 'office/project_details.html', {'project': project})
