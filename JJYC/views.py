from django.shortcuts import render
from mainApp.models import Projects, Announcement
from django.contrib import messages

def index(request):
    ongoing_projects = Projects.objects.filter(is_completed=False)

    latest_announcement = Announcement.objects.latest('id')

    modal_data = latest_announcement
    if not request.session.get('modal_shown', False):
        request.session['modal_shown'] = True
    else:
        messages.success(request, "No Data")

    context = {
        'ongoing_projects': ongoing_projects,
        'modal_data': modal_data,
    }

    return render(request, 'mainApp/index.html', context)



