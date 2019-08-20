from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
def home_page(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'projects': Project.objects.all()})


def all_projects_page(request):
    return render(request=request,
                  template_name='main/all_projects.html',
                  context={'projects': Project.objects.all()})


def single_project_page(request, current_slug):
    project_slugs = [project.project_slug for project in Project.objects.all()]

    if current_slug in project_slugs:
        current_project = Project.objects.get(project_slug=current_slug)
        return render(request=request,
                      template_name='main/single_project.html',
                      context={'project': current_project})

    return HttpResponse(f"{current_slug} does not exist!")
