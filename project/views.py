from django.shortcuts import render

import project

# Create your views here.
from .models import project



def projects_list(request):
    projects = project.objects.all()
    return render(request, 'projects_list.html', {'projects': projects})
