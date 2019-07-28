from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BaseTemplateView(TemplateView):
    template_name = 'images_and_videos/base.html'
