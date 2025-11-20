from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import VisualNovel
from .models import User
# Replace ModelName in the above line
# with the name of your model in models.py

admin.site.register(VisualNovel)
# Replace ModelName in the above line
# with the name of your model in models.py

admin.site.register(User)
