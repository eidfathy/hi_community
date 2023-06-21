from django.contrib import admin
from .models import User, UserProfile, PlacesProfile, InterestUser, InterestPlaces

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(PlacesProfile)
admin.site.register(InterestUser)
admin.site.register(InterestPlaces)

