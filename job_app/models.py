from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    requirements = models.TextField(max_length=150)
    salary = models.CharField(max_length=150)
    level = models.CharField(max_length=150)

def __str__(self):
    return self.title

