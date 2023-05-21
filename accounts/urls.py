from django.urls import path
from .views import registeruser, register, registerplaces, custom_login, user_profile, places_profile
app_name = 'accounts'

urlpatterns = [
    path('login/', custom_login, name='login'),
    
    path('register/', register, name='register'),
    path('registeruser/', registeruser, name='registeruser'),
    path('registerplaces/', registerplaces, name='registerplaces'),
    
    
    # path('signup/', signup, name='signup'),
    
    path('userprofile/<int:profile_id>/', user_profile, name='userprofile'),
    path('placesprofile/<int:places_profile_id>/', places_profile, name='placesprofile'),

]

