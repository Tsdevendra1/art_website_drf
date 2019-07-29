from django.db import models

GENERAL = 'G'
SKETCHBOOK = 'S'
EXHIBITION = 'E'
TEACHING = 'T'
PROJECT_TYPES = (
    (GENERAL, 'General'),
    (SKETCHBOOK, 'Sketchbook'),
    (EXHIBITION, 'Exhibition'),
    (TEACHING, 'Teaching'),
)


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.FileField()
    banner = models.FileField()
    video = models.FileField()
    project_type = models.CharField(max_length=13, choices=PROJECT_TYPES, default=GENERAL)
    date = models.DateField()


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    picture = models.FileField()
