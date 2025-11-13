from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import VisualNovels
from .models import Users
# Replace ModelName in the above line
# with the name of your model in models.py

admin.site.register(VisualNovels)
# Replace ModelName in the above line
# with the name of your model in models.py

admin.site.register(Users)
