from django.shortcuts import render

from office.models import Projects

def index(request):
    print("here")
    ongoing_projects = Projects.objects.filter(is_completed=False)

    # Loop through the queryset and print information including the photo
    for project in ongoing_projects:
        print(f"Project: {project.title}")
        print(f"Description: {project.description}")
        print(f"Photo: {project.photos.url}")  # Access the URL of the photo
        # Add more fields as needed

    # You can also pass the projects to the context if you need them in the template
    context = {
        'ongoing_projects': ongoing_projects,
    }

    # Render the index page with the ongoing projects
    return render(request, 'office/index.html', context)




