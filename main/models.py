from django.db import models
from datetime import datetime


# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_content = models.TextField()
    project_github_url = models.CharField(max_length=200)
    project_slug = models.CharField(max_length=200)
    project_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.project_title
