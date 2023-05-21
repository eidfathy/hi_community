from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Post_User, Comment_Post_User, Like_Post_User
from .forms import CreatePostForm, CreateCommentForm

from audioop import reverse
from ctypes.wintypes import HINSTANCE


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterUserForm, UserProfileForm, PlacesProfileForm, RegisterPlacesForm, LoginForm
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, PlacesProfile


from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, EditPostForm, LikePostForm, UnlikePostForm

@login_required
def create_post(request):
    """
    View function to create a new post.
    """
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creater = request.user.userprofile
            post.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required 
@csrf_exempt
def edit_post(request, post_id):
    """
    View function to edit a post.
    """
    try:
        post = Post_User.objects.get(id=post_id, creater__user=request.user)
    except Post_User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            post_text = post.content_text if post.content_text else False
            post_image = post.image.url if post.image else False
            return JsonResponse({
                "success": True,
                "text": post_text,
                "picture": post_image
            })
    else:
        form = EditPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@csrf_exempt
def like_post(request, id):
    """
    View function to like a post.
    """
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post_User.objects.get(pk=id)
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                post.likers.add(user_profile)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def unlike_post(request, id):
    """
    View function to unlike a post.
    """
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post_User.objects.get(pk=id)
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                post.likers.remove(user_profile)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))













































# def user_profile(request):
#     # عرض الملف الشخصي للمستخدم مع جميع المنشورات
#     posts = Post_User.objects.filter(UserProfile=request.user.userprofile)
#     context = {
#         'posts': posts
#     }
#     return render(request, 'user_profile.html', context)

# def create_post(request):
#     # إنشاء منشور جديد
#     if request.method == 'POST':
#         form = CreatePostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.UserProfile = request.user.userprofile
#             post.save()
#             return redirect('user_profile')
#     else:
#         form = CreatePostForm()
    
#     context = {
#         'form': form
#     }
#     return render(request, 'create_post.html', context)

# def create_comment(request, post_id):
#     # إنشاء تعليق على منشور معين
#     post = Post_User.objects.get(id=post_id)
#     if request.method == 'POST':
#         form = CreateCommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.UserProfile = request.user.userprofile
#             comment.save()
#             return redirect('user_profile')
#     else:
#         form = CreateCommentForm()
    
#     context = {
#         'form': form,
#         'post': post
#     }
#     return render(request, 'create_comment.html', context)

# def like_post(request, post_id):
#     # إضافة أو إزالة إعجاب المستخدم بمنشور معين
#     post = Post_User.objects.get(id=post_id)
#     user_profile = request.user.userprofile
#     if user_profile in post.likes.all():
#         post.likes.remove(user_profile)
#     else:
#         post.likes.add(user_profile)
#     return redirect('user_profile')
