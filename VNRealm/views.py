
# Create your views here.
#from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login#, logout
from django.shortcuts import render, redirect
from .models import VisualNovel, Review
from django.http import Http404
# Replace ModelName in the above line
# with the name of your model in models.py

def index(request):
    records = VisualNovel.objects.all()
    if not (request.user.is_authenticated and request.user.UserProfile.is_adultPlus):
        records = records.filter(is_adult=False)
    # Replace ModelName in the above line
    # with the name of your model in models.py
    return render(request, 'index.html', {'records': records})


def vn_detail(request, dt):
    try:
        vn = VisualNovel.objects.get(id=dt)
        reviews = vn.reviews.all()
    except VisualNovel.DoesNotExist:
        raise Http404("Visual Novel not found")

    request.session['last_vn_id'] = dt

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        content = request.POST.get('content')
        Review.objects.create(vn=vn, content=content, user=request.user )  # no user yet
        return redirect('VN_detailpage', dt=dt)

    reviews = vn.reviews.all()
    return render(request, 'VN_detailpage.html', {'vn': vn, 'reviews': reviews})

def login_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not username or not password:
                return render(request, "login.html", {"error": "Username and password required"})

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next', '/Home')  # after login go back
                return redirect(next_page)
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials.'})

        elif 'signup' in request.POST:  # Signup form submitted
            username = request.POST.get('signup_username')
            password1 = request.POST.get('signup_password')
            password2 = request.POST.get('signup_password2')

            if password1 != password2:
                  return render(request, 'login.html', {'error': 'Passwords must match.'})
            # Optionally: validate username/password, check if exists
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password1)
                login(request, user)
                next_page = request.GET.get('next', '/Home')
                return redirect(next_page)
            else:
                return render(request, 'login.html', {'error': 'Username already exists.'})

    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'Home.html')
