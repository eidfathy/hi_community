from audioop import reverse
import datetime
from django.db import models
from accounts.models import UserProfile, PlacesProfile
from datetime import datetime


def image_post_user(instance,filename):
    imgename , extension = filename.split(".")
    return "image_post_user/%s.%s"%(instance.id, extension)

class Post(models.Model):
    creater = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="createdpost")
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=image_post_user)
    created_at = models.DateTimeField(default=datetime.now)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{str(self.creater)} Create Post=> {str(self.description)}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    creater = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="createdcomment")
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f" {str(self.creater)}  Comment In Post=> {str(self.post)}"

class Like(models.Model):
    creater = models.ForeignKey(UserProfile, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{str(self.creater)}  Like In Post=> {str(self.post)}"
    



class PostPlaces(models.Model):
    creater = models.ForeignKey(PlacesProfile, on_delete=models.CASCADE, related_name="createdpost")
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=image_post_user)
    created_at = models.DateTimeField(default=datetime.now)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{str(self.creater)} Create Post=> {str(self.description)}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


