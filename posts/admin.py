from django.contrib import admin
from .models import PostUser, CommentPostUser, LikePostUser

# Register your models here.
admin.site.register(PostUser)
admin.site.register(CommentPostUser)
admin.site.register(LikePostUser)