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


class ImageModelViewset(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
