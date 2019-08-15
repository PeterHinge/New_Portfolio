from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ['project_title', 'project_published']}),
        ("Content", {'fields': ['project_description', 'project_content', 'project_thumbnail']}),
        ("URLs", {'fields': ['project_github_url', 'project_slug']})
    ]


admin.site.register(Project, ProjectAdmin)
