from zoneinfo import available_timezones

from django.db import models

#Create your models here.


from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class AvailableOn(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class VisualNovel(models.Model):
    title = models.CharField(max_length=300, default="titlegoeshere")
    author = models.ManyToManyField(Author, blank=True)
    release_year = models.IntegerField(default=0000)
    genre = models.ManyToManyField(Genre, blank=True)
    is_adult = models.BooleanField(default=False)  # 18+ yes/no
    available_on = models.ManyToManyField(AvailableOn, blank=True)
    cover_image = models.ImageField(upload_to='vn_covers/', blank=True, null=True)
    def __str__(self):
       genres = ", ".join([g.name for g in self.genre.all()])
       authors = ", ".join([a.name for a in self.author.all()])
       available_ons = ", ".join([ab.name for ab in self.available_on.all()])
       return (f"TITLE: {self.title} "
               f"AUTHOR: {authors} "
               f"RELEASE YEAR: ({self.release_year}) "
               f"GENRE: {genres} "
               f"Available On: {available_ons}")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, default="HEWHOSHALLNOTBENAMED")
    user_Interests = models.CharField(max_length=100, default="Nothing Really")
    is_adultPlus = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True) #
    def __str__(self):
        return f"{self.Name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    vn = models.ForeignKey(VisualNovel, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.vn}"