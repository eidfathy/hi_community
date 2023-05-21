# from django.shortcuts import render, redirect
# from .models import Post_User, Comment_Post_User, Like_Post_User
# from .forms import CreatePostForm, CreateCommentForm

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
