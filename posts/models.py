from audioop import reverse
from datetime import timezone
import datetime
from sys import setprofile
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import User, UserProfile, PlacesProfile
from datetime import datetime

def image_post_user(instance,filename):
    imgename , extension = filename.split(".")
    return "image_post_user/%s.%s"%(instance.id, extension)

class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=image_post_user)
    created_at = models.DateTimeField(default=datetime.now)
    creater = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="createdpost")
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{str(self.description)}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    creater = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="createdcomment")
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f"{str(self.creater)} - {str(self.post)}"

class Like(models.Model):
    user = models.ForeignKey(UserProfile, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{str(self.user)} - {str(self.post)}"






