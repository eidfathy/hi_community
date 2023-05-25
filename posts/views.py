from django.views import View
from audioop import reverse
from ctypes.wintypes import HINSTANCE
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, UserProfile
from .forms import PostForm


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'post_detail.html', {'post': post, 'user_profile': user_profile})










