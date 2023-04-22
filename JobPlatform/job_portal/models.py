from django.db import models

# Create your models here.
class jobsInfo(models.Model):
    title = models.CharField(max_length=50, default="", null=False)
    location = models.CharField(max_length=50, null=False)
    companyName = models.CharField(max_length=50, default="", null=False)
    responsibilities = models.CharField(max_length=150, default="", null=False)
    requirements = models.CharField(max_length=150, default="", null=False)
   
    def __str__(self):
        return self.title
  