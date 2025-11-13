from django.db import models

# Create your models here.
from django.db import models
class VisualNovels(models.Model):
    def __str__(self):
        return self.author
class Users(models.Model):
    def __str__(self):
        return self.threads