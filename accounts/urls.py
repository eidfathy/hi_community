from django import views
from django.urls import path
from .views import registeruser, register, registerplaces, custom_login, user_profile, places_profile, logout_view, create_post, home
app_name = 'accounts'

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('home/', home, name='home'),
    
    path('register/', register, name='register'),
    path('registeruser/', registeruser, name='registeruser'),
    path('registerplaces/', registerplaces, name='registerplaces'),
    
    # path('signup/', signup, name='signup'),
    
    path('userprofile/<int:profile_id>/', user_profile, name='userprofile'),
    path('placesprofile/<int:places_profile_id>/', places_profile, name='placesprofile'),
    
    # path('', post_user_list, name = 'post_list'),
    path('create_post/', create_post, name='create_post')
    

]

