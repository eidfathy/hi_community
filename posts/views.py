from django.shortcuts import render
from .models import Post
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required


# @login_required
# def post_user_list(request):
#     post_user_list = Post.objects.all()
#     # current_user = request.user
#     # post_user_list = Post.objects.filter(creater=current_user)
#     context = {'posts':post_user_list} # tempate name
#     return render(request, 'post_user_list.html', context)

# @login_required
# def post_user_detail(request, id):
#     post_user_detail = Post.objects.get(id=id)
#     context = {'post':post_user_detail}
#     return render(request, 'post_user_detail.html', context)



