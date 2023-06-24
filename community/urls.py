from django.urls import path

from .views import community_profile, community, create_community
app_name = 'community'

urlpatterns = [
    path('community/', community, name = 'community'),
    
    path('create_community/', create_community, name='create-community'),
    
    path('community/<uuid:community_id>/', community_profile, name='communityprofile'),
    
    # {% url 'community:communityprofile' community_id=community.id %}
    
]
