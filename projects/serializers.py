from rest_framework import serializers

from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    thumbnail = serializers.FileField()
    banner = serializers.FileField()
    video = serializers.FileField()

    class Meta:
        model = Project
        fields = ['title', 'description', 'thumbnail_aws_path', 'banner_aws_path', 'video_aws_path', 'project_type',
                  'date']

    def create(self, validated_data):
        thumbnail = validated_data.pop('thumbnail')
        banner = validated_data.pop('banner')
        video = validated_data.pop('video')

