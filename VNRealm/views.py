
# Create your views here.
#from django.shortcuts import render, HttpResponse


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login#, logout
from django.shortcuts import render, redirect
from .models import VisualNovel, Review
from django.http import Http404
# Replace ModelName in the above line
# with the name of your model in models.py

def index(request):
    records = VisualNovel.objects.all()
    # Replace ModelName in the above line
    # with the name of your model in models.py
    return render(request, 'index.html', {'records': records})


def vn_detail(request, dt):
    try:
        vn = VisualNovel.objects.get(id=dt)
        reviews = vn.reviews.all()
    except VisualNovel.DoesNotExist:
        raise Http404("Visual Novel not found")
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        content = request.POST.get('content')
        Review.objects.create(vn=vn, content=content)  # no user yet
        return redirect('VN_detailpage', dt=dt)

    reviews = vn.reviews.all()
    return render(request, 'VN_detailpage.html', {'vn': vn, 'reviews': reviews})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_page = request.GET.get('next', 'VN_detailpage')  # after login go back
            return redirect(next_page)
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials.'})

    return render(request, 'login.html')

#def logout_view(request):
    logout(request)
    return redirect('login')