from zoneinfo import available_timezones

from django.db import models

#Create your models here.


from django.conf import settings
from django.db import models
class VisualNovel(models.Model):
    title = models.CharField(max_length=300, default="titlegoeshere")
    author = models.CharField(max_length=100, default="Noone")
    release_year = models.IntegerField(default=0000)
    genre = models.CharField(max_length=100, default="Unknown")
    is_adult = models.BooleanField(default=False)  # 18+ yes/no
    available_on = models.CharField(max_length=100, default="unavailable")
    def __str__(self):
        return (f"TITLE: {self.title} "
                f"AUTHOR: {self.author} "
                f"RELEASE YEAR: ({self.release_year})"
                f"GENRE: {self.genre} "
                f"Available On: {self.available_on} ")
class UserProfile(models.Model):
    Name = models.CharField(max_length=100, default="HEWHOSHALLNOTBENAMED")
    User_Interests = models.CharField(max_length=100, default="Nothing Really")
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True) #
    def __str__(self):
        return (f"{self.Name}")




