from django.urls import path

from .import views
app_name = 'community'

urlpatterns = [
    path('community/', views.community, name = 'community'),
    
    path('create_community/', views.create_community, name='create_community'),
    
    path('communityprofile/<int:community_id>/', views.community_profile, name='communityprofile'),
    # {% url 'community:communityprofile' community_id=community.id %}
    
]
