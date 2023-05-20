from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# pip install django==3.2
from django.db.models.signals import post_save
from django.dispatch import receiver


CHOICES_ROLE = [
    ('user_profile', 'user_profile'),
    ('places_profile', 'places_profile'),
]

class User(AbstractUser):
    role = models.CharField(max_length=20, null=True, choices=CHOICES_ROLE)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, unique=False)
    last_name = models.CharField(max_length=30, unique=False)
    email = models.EmailField(_('email address'), max_length=254, unique=True, null=True, blank=True)
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def __str__(self) -> str:
        return self.username 

# # #####################################################
# # #####################################################

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
]

def image_user(instance,filename):
    imgename , extension = filename.split(".")
    return "profile_user/%s.%s"%(instance.id, extension)

class UserProfile(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    image = models.ImageField(upload_to=image_user)
    phone_number = models.CharField(max_length=15,)
    birth_day = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=7, choices=GENDER_CHOICES)
    address = models.CharField(max_length = 50, blank = True, null = True)
    country = models.CharField(max_length=15,)
    area = models.CharField(max_length=10,)
    education = models.CharField(max_length=30,)
    job_tite = models.CharField(max_length=15,)
    about_me = models.TextField(max_length=1000, null=True,)
    #interests
    published_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username if self.user else 'No User'

# # # ################################################
# # # ################################################

def image_places(instance,filename):
    imgename , extension = filename.split(".")
    return "profile_places/%s.%s"%(instance.id, extension)

class PlacesProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    image = models.ImageField(upload_to=image_places)
    nameplaces = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15,)
    type = models.CharField(max_length=7, choices=GENDER_CHOICES)
    #location
    address = models.CharField(max_length = 50, blank = True, null = True)
    country = models.CharField(max_length=15,)
    area = models.CharField(max_length=10,)
    sarves = models.CharField(max_length=150,)
    #interests
    about_me = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username if self.user else 'No User'




#######################################################
#######################################################

# create new user ---> create new empty profile
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.role == 'user_profile':
#             user_profile, created = UserProfile.objects.get_or_create(User=instance)
#             user_profile.save() 
#         elif instance.role == 'places_profile':
#             places_profile, created = PlacesProfile.objects.get_or_create(User=instance)
#             places_profile.save()

# post_save.connect(create_user_profile, sender=User)