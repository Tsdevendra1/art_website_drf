from typing import Dict

from rest_framework import serializers

from projects.models import Project, Image


class ProjectSerializer(serializers.ModelSerializer):
    # TODO: Add image relation field to get image set for a project
    class Meta:
        model = Project
        fields = ['title', 'description', 'thumbnail_aws_path', 'banner_aws_path', 'video_aws_path', 'project_type',
                  'date']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['project', 'picture']
