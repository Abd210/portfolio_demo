from django.shortcuts import render

import project

# Create your views here.
from .models import project
from django.shortcuts import render, get_object_or_404

def project_detail(request, project_id):
    project_obj = get_object_or_404(project, id=project_id)
    return render(request, 'project_detail.html', {'project': project_obj})



def home_page(request):
    projects = project.objects.all()  # Fetch your projects
    return render(request, 'home.html', {'projects': projects})
