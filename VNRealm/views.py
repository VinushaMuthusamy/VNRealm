
#default django user implemented
from django.contrib.auth.models import User
#login requirement and authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

#forms from forms.py for played list for user and profile pic form
from .forms import PlayedListForm, UserProfileForm
#all required models
from .models import VisualNovel, Review, UserProfile, PlayedList
#http unknown response
from django.http import Http404

#index html page view
def index(request):
    #all visual novels displayed in the main page
    records = VisualNovel.objects.all()
    #if user is authenticated and adult vn is toggled true, adult vns appear
    #otherwise they don't
    if request.user.is_authenticated:
        #check if profile exist first
        if UserProfile.objects.filter(user=request.user).exists():
            profile = UserProfile.objects.get(user=request.user)
        else:
            profile = UserProfile.objects.create(user=request.user)
        if not profile.is_adultPlus:
            records = records.filter(is_adult=False)
    else:
        #not logged in hide adult vn
        records = records.filter(is_adult=False)
    return render(request, 'index.html', {'records': records})


#VN_detailpage html view
def vn_detail(request, dt):
    #visual novel displayed depending on selected id which is activated
    try:
        vn = VisualNovel.objects.get(id=dt)
        reviews = vn.reviews.all()
    except VisualNovel.DoesNotExist:
        raise Http404("Visual Novel not found")

    #recent session is saved for resuming
    request.session['last_vn_id'] = dt

    #for posting reviews the user must log in
    #after login review gets posted
    if request.method == 'POST':
        #no account redirect to login page
        if not request.user.is_authenticated:
            return redirect('login')
        content = request.POST.get('content')        #if no user yet
        Review.objects.create(vn=vn, content=content, user=request.user )
        return redirect('VN_detailpage', dt=dt)

    reviews = vn.reviews.all()
#reviews and the vn with selected id is visible on the current session of the page
    return render(request, 'VN_detailpage.html', {'vn': vn, 'reviews': reviews})


#login html page view
def login_view(request):
    #username and password is requested
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
    #if nothing filled and login clicked error appears
            if not username or not password:
                return render(request, "login.html", {"error": "Username and password required"})

    #after entering credentials its authenticated
            user = authenticate(request, username=username, password=password)
    #checks existing user info
            if user is not None:
                login(request, user)
                # after login go back
                next_page = request.GET.get('next', '/Home')
                if "/" == next_page[0]:
                    return redirect(next_page)
                else:
                    return render(request, 'login.html')

            else:
                return render(request, 'login.html', {'error': 'Invalid username/password'})

        #signup form submission
        elif 'signup' in request.POST:
            username = request.POST.get('signup_username')
            password1 = request.POST.get('signup_password')
            password2 = request.POST.get('signup_password2')

        #to add password and another password to confirm correctly
            if password1 != password2:
                  return render(request, 'login.html', {'error': 'passwords must match.'})
            #validating username/password, checking if it exists
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password1)
                login(request, user)
                #go back after signup
                next_page = request.GET.get('next', '/Home')
                return redirect(next_page)
            else:
                return render(request, 'login.html', {'error': 'Username already exists.'})

    return render(request, 'login.html')

#login required to view home page
@login_required
def home(request):
    #request user for page, page is unique to each user
    user = request.user
    profile_qs = UserProfile.objects.filter(user=user)

    #if profile exists for user --> get it
    if profile_qs.exists():
        profile = profile_qs.first()
    else:
        # if not --> create one
        profile = UserProfile.objects.create(user=user)

#toggling adult vn visibility by user
    if request.method == 'POST':
        is_adult = request.POST.get('is_adultPlus') == 'on'
        profile.is_adultPlus = is_adult
        profile.save()

#profile picture upload through forms
    #request.Files , template used from django documentation
    #cite: https://docs.djangoproject.com/en/5.2/topics/http/file-uploads/
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = UserProfileForm(instance=profile)

#play list made by selecting vns and saved through forms
    #django template forms used for listing
    if request.method == 'POST':
        form = PlayedListForm(request.POST)
        if form.is_valid():
            played_item = form.save(commit=False)
            #set it to current user
            played_item.user = user
            played_item.save()
    else:
        form = PlayedListForm()

    #rating vns in the played list and update rating in home view
    if request.method == 'POST':
        if 'played_id' in request.POST:
            played_id = request.POST.get('played_id')
            rating = request.POST.get('rating')
            played_item = PlayedList.objects.get(id=played_id, user=user)
            #after rating set save as integer
            if rating:
                played_item.rating = int(rating)
                played_item.save()

#showing only selected vns
    played_vns = PlayedList.objects.filter(user=user).select_related('vn')

#delete from list
    if request.method == 'POST':
        if 'delete_played_id' in request.POST:
            played_id = request.POST.get('delete_played_id')
            played_item = PlayedList.objects.get(id=played_id, user=user)
            played_item.delete()

    return render(request, 'Home.html',
                  {'profile': profile, 'form': form,
                   'played_vns': played_vns, 'profile_form': profile_form})


#post login
@login_required
def delete_review(request, review_id):
    #getting respective review to delete
    try:
        review = Review.objects.get(id=review_id, user=request.user)  # only allow owner
        review.delete()
    except Review.DoesNotExist:
        pass
    return redirect('VN_detailpage', dt=review.vn.id)

