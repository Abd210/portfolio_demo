from django.shortcuts import render

import project

from .models import project
from django.shortcuts import render, get_object_or_404

# this is the view for the project detail
def project_detail(request, project_id):
    project_obj = get_object_or_404(project, id=project_id)
    return render(request, 'project_detail.html', {'project': project_obj})

#this is the view for the home page
def home_page(request):
    projects = project.objects.all()  # Fetch your projects
    return render(request, 'home.html', {'projects': projects})
