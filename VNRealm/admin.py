from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import VisualNovel, Genre, Author, AvailableOn, Review
from .models import UserProfile
# Replace ModelName in the above line
# with the name of your model in models.py

admin.site.register(VisualNovel)
# Replace ModelName in the above line
# with the name of your model in models.py
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(AvailableOn)
admin.site.register(UserProfile)
admin.site.register(Review)