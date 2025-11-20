from django.db import models

#Create your models here.


from django.conf import settings
from django.db import models
class VisualNovel(models.Model):
    title = models.CharField(max_length=300, default="titlegoeshere")
    author = models.CharField(max_length=100, default="Noone")
    release_year = models.IntegerField(default=0000)
    def __str__(self):
        return f"{self.title} by {self.author} ({self.release_year})"
class User(models.Model):
    Name = models.CharField(max_length=100, default="HEWHOSHALLNOTBENAMED")
    User_Interests = models.CharField(max_length=100, default="Nothing Really")
    def __str__(self):
        return f"{self.Name} by {self.User_Interests}"




