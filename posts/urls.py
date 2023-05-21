from django.urls import path
from .views import create_post, edit_post, like_post, unlike_post

app_name = 'posts'

urlpatterns = [
    path('create-post/', create_post, name='create_post'),
    path('edit-post/<int:post_id>/', edit_post, name='edit_post'),
    path('like-post/<int:id>/', like_post, name='like_post'),
    path('unlike-post/<int:id>/', unlike_post, name='unlike_post'),
]
