from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render, HttpResponse

#def index(request):
  #  return HttpResponse('<h1>HELLO WORLD!</h1>')

from django.shortcuts import render, redirect
from .models import VisualNovel
# Replace ModelName in the above line
# with the name of your model in models.py

def index(request):
    records = VisualNovel.objects.all()
    # Replace ModelName in the above line
    # with the name of your model in models.py
    return render(request, 'index.html', {'records': records})
