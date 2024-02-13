from django.contrib import admin
from . models import Announcement, Projects

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'partners', 'total_budget','status')

    search_fields = ('title' , 'partners', 'status')

admin.site.register(Projects, ProjectsAdmin)



class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

    search_fields = ('title' , 'url')
admin.site.register(Announcement, AnnouncementAdmin)

