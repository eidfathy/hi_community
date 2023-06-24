from audioop import reverse
from ctypes.wintypes import HINSTANCE
from urllib import request
from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterUserForm, UserProfileForm, PlacesProfileForm, RegisterPlacesForm, LoginForm, NewPostForm
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, PlacesProfile
from django.urls import reverse_lazy
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import logout
from posts.models import Post, PostPlaces
from community.models import Community


User = get_user_model()

def register(request):
    return render(request, 'register.html', {})




def registeruser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST , request.FILES)
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
            return redirect('accounts:userprofile', profile_id=user_profile.id)
    else:
        form = RegisterUserForm()
        user_profile_form = UserProfileForm()
    return render(request, 'registeruser.html', {'form': form, 'user_profile_form' : user_profile_form})


def registerplaces(request):
    if request.method == 'POST':
        form = RegisterPlacesForm(request.POST)
        places_profile_form = PlacesProfileForm(request.POST , request.FILES)
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
            return redirect('accounts:placesprofile', places_profile_id=places_profile.id)
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
    post_user_list = Post.objects.all()
    post_user = Post.objects.filter(creater=profile)
    context = {'profile':profile, 'posts':post_user_list, "postuser":post_user} 
    return render(request, 'profile_user.html', context)


@login_required
def places_profile(request, places_profile_id):
    places_profile = get_object_or_404(PlacesProfile, id=places_profile_id, user=request.user)
    post_places_list = PostPlaces.objects.all()
    post_community = PostPlaces.objects.filter(creater=places_profile)
    context = {'places_profile': places_profile, 'postsplaces': post_places_list, "postcommunity":post_community}
    return render(request, 'profile_places.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')  

@login_required
def create_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.creater = request.user
            new_post.save()
            return redirect('userprofile', pk=new_post.id)
    else:
        newpost = NewPostForm()
        
    context = {'form': form}
    return render(request, 'profile_user.html', context)


@login_required
def home(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    post_list_all = list(Post.objects.all()) + list(PostPlaces.objects.all()) 
    community = Community.objects.filter(creator=profile)
    context = {'profile': profile, 'posts': post_list_all, "community":community}
    return render(request, 'home.html', context)

@login_required
def homeplaces(request):
    places_profile = get_object_or_404(PlacesProfile, user=request.user)
    post_places_list = PostPlaces.objects.all()
    context = {'places_profile': places_profile, 'postsplaces': post_places_list}
    return render(request, 'homeplaces.html', context)

# def registeruser2(request):
#     return render(request, 'registeruser2.html', {})
