from audioop import reverse
from django.db import models
from accounts.models import User, UserProfile
import uuid
from datetime import datetime
from django.utils.text import slugify

class InterestCommunity(models.Model):
	title = models.CharField(max_length=75, verbose_name='interest_community')
	slug = models.SlugField(null=False, unique=True)

	class Meta:
		verbose_name='interest_community'
		verbose_name_plural = 'interest_community'

	def get_absolute_url(self):
		return reverse('interest_community', args=[self.slug])
		
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

def image_community(instance,filename):
    imgename , extension = filename.split(".")
    return "image_post_user/%s.%s"%(instance.id, extension)

class Community(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(UserProfile, related_name='joined_groups')
    name_community = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True) 
    description = models.TextField()
    image = models.ImageField(upload_to=image_community)
    created_at = models.DateTimeField(default=datetime.now)
    interest = models.ManyToManyField(InterestCommunity, related_name='interests')

    def __str__(self):
        return f"{str(self.creator)}| Create => {str(self.name_community)}| Id => {str(self.id)}"
    
    @property
    def member_count(self):
        return self.members.count()

class CommunityMembership(models.Model):
    group = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.group.name}'

class PostCommunity(models.Model):
    group = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content