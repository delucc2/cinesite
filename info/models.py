from django.db import models

# Create your models here.
class Information(models.Model):
    bylaws = models.FileField()
    policies = models.FileField()
