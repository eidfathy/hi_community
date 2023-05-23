from .models import PostUser, CommentPostUser, LikePostUser
from audioop import reverse
from ctypes.wintypes import HINSTANCE

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model

from accounts.models import User
from django.contrib.auth.decorators import login_required




from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import PostUser, CommentPostUser, LikePostUser

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creater = request.user.userprofile
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def post_detail(request, post_id):
    post = PostUser.objects.get(id=post_id)
    comments = CommentPostUser.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commenter = request.user.userprofile
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def like_post(request, post_id):
    post = PostUser.objects.get(id=post_id)
    like, created = LikePostUser.objects.get_or_create(post=post, user_profile=request.user.userprofile)
    if created:
        post.likes.add(like)
    else:
        post.likes.remove(like)
    return redirect('post_detail', post_id=post.id)

@login_required
def delete_post(request, post_id):
    post = PostUser.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')  # Replace 'home' with the appropriate URL or name of the home page
    return render(request, 'delete_post.html', {'post': post})

@login_required
def unlike_post(request, post_id):
    post = PostUser.objects.get(id=post_id)
    like = LikePostUser.objects.get(post=post, user_profile=request.user.userprofile)
    post.likes.remove(like)
    like.delete()
    return redirect('post_detail', post_id=post.id)



def post_list(request):
    post_list = PostUser.objects.all()
    return render(request, )





