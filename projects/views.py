from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.response import Response

from projects.models import Project
from projects.serializers import ProjectSerializer


class BaseTemplateView(TemplateView):
    template_name = 'projects/base.html'


class ProjectModelViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ImageModelViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    # TODO: Need to return the project id then post the images when the project id in the json so to save the foreign key
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
