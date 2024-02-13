from django.shortcuts import render
from .models import Projects

from django.views.generic import ListView
from .models import Announcement

def announcement(request):
    # Retrieve the most recent announcement
    announcement = Announcement.objects.latest('id')
    return render(request, 'mainApp/index.html', {'announcement': announcement})


def contact(request):
    return render(request, 'mainApp/contact.html')


def projects(request):
    ongoing_project = Projects.objects.filter(is_completed=False)

    context = {
        'ongoing_project': ongoing_project,
    }

    return render(request, 'mainApp/projects.html', context)

def completed_projects(request):
    return render(request, 'mainApp/completed_projects.html')


def project_details(request):
    return render(request, 'mainApp/project_details.html')

def about(request):
    return render(request, 'mainApp/about.html')

def gallery(request):
    return render(request, 'mainApp/gallery.html')


class ProjectListView(ListView):
    model = Projects
    template_name = 'mainApp/projects.html'  # The template to render
    context_object_name = 'projects'  # The variable name to use in the template