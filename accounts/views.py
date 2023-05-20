from audioop import reverse
from ctypes.wintypes import HINSTANCE
from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterUserForm, UserProfileForm, PlacesProfileForm, RegisterPlacesForm, LoginForm
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, PlacesProfile
from django.urls import reverse_lazy
from django.conf import settings
from django.db.models.signals import post_save

User = get_user_model()

def register(request):
    return render(request, 'register.html', {})

# def profile_user(request):
#     return render(request, 'profile_user.html', {})

# def profile_places(request):
#     return render(request, 'profile_places.html', {})

def registeruser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if form.is_valid() and user_profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) 
            user.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user= user 
            user_profile.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('accounts:login')
    else:
        form = RegisterUserForm()
        user_profile_form = UserProfileForm()
    return render(request, 'registeruser.html', {'form': form, 'user_profile_form' : user_profile_form})


def registerplaces(request):
    if request.method == 'POST':
        form = RegisterPlacesForm(request.POST)
        places_profile_form = PlacesProfileForm(request.POST)
        if form.is_valid() and places_profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) 
            user.save()
            places_profile = places_profile_form.save(commit=False)
            places_profile.user = user 
            places_profile.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('accounts:login')
    else:
        form = RegisterPlacesForm()
        places_profile_form = PlacesProfileForm()
    return render(request, 'registerplaces.html', {'form': form, 'places_profile_form': places_profile_form})



def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if user.role == 'user_profile':
                    try:
                        user_profile = UserProfile.objects.get(user=user)
                        return redirect('accounts:userprofile', user_profile.id)
                    except UserProfile.DoesNotExist:
                        pass
                elif user.role == 'places_profile':
                    try:
                        places_profile = PlacesProfile.objects.get(user=user)
                        return redirect('accounts:placesprofile', places_profile.id)
                    except PlacesProfile.DoesNotExist:
                        pass
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



@login_required
def user_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
    return render(request, 'profile_user.html', {'profile': profile})

@login_required
def places_profile(request, places_profile_id):
    places_profile = get_object_or_404(PlacesProfile, id=places_profile_id, user=request.user)
    return render(request, 'profile_places.html', {'places_profile': places_profile})









# @receiver(post_save, sender=User)
# def create_or_save_profile(sender, instance, created, **kwargs):
#     try:
#         user_profile = UserProfile.objects.get(User=instance)
#         user_profile.save()
#     except UserProfile.DoesNotExist:
#         UserProfile.objects.create(user=instance)

#     try:
#         places_profile = PlacesProfile.objects.get_or_create(User=instance)
#         places_profile.save()
#     except PlacesProfile.DoesNotExist:
#         pass




# def registeruser(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         user_profile_form = UserProfileForm(request.POST)
#         if form.is_valid() and user_profile_form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1']) 
#             user.save()
#             user_profile = user_profile_form.save(commit=False)
#             user_profile.user = user 
#             user_profile.save()
#             user_id = user.id  # Get the user ID
#             # Create the user profile using the ID
#             UserProfile.objects.create(user_id=user_id)
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('userprofile')
#     else:
#         form = RegisterUserForm()
#         user_profile_form = UserProfileForm()
#     return render(request, 'registeruser.html', {'form': form, 'user_profile_form' : user_profile_form})


# def registerplaces(request):
#     if request.method == 'POST':
#         form = RegisterPlacesForm(request.POST)
#         places_profile_form = PlacesProfileForm(request.POST)
#         if form.is_valid() and places_profile_form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1']) 
#             user.save()
#             places_profile = places_profile_form.save(commit=False)
#             places_profile.user = user 
#             places_profile.save()
#             places_id = user.id  # Get the user ID
#             # Create the user profile using the ID
#             UserProfile.objects.create(places_id=places_id)
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         if user is not None:
#             login(request, user)
#             return redirect('placesprofile')
#     else:
#         form = RegisterPlacesForm()
#         places_profile_form = PlacesProfileForm()
#     return render(request, 'registerplaces.html', {'form': form, 'places_profile_form': places_profile_form})
