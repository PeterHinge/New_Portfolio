from django.db import models
from datetime import datetime


# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_published = models.DateTimeField('date published', default=datetime.now())
    project_description = models.CharField(max_length=300)
    project_content = models.TextField()
    project_slug = models.CharField(max_length=100)
    project_github_url = models.CharField(max_length=100)
    project_thumbnail = models.CharField(max_length=100, default="no_image")

    def __str__(self):
        return self.project_title
