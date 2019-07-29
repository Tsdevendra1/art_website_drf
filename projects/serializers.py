from typing import Dict

from rest_framework import serializers

from projects.models import Project, Image


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['picture']


class ProjectSerializer(serializers.ModelSerializer):
    # TODO: Maybe change this to a different type of field so it returns the hyperlinks, but actually this method is better becaus eyou can do the entire request in one post
    images = ImagesSerializer(many=True)

    class Meta:
        model = Project
        fields = ['title', 'description', 'thumbnail_aws_path', 'banner_aws_path', 'video_aws_path', 'project_type',
                  'date', 'images']

    def create(self, validated_data):
        # Image data should be an array of dictionaries which fit the serializer specified
        images_data = validated_data.pop('images')
        # TODO: Maybe have error here if no images_data?
        project = Project.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(project=project, **image_data)
        return project
