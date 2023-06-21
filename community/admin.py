from django.contrib import admin
from .models import Community, CommunityMembership, PostCommunity


admin.site.register(Community)
admin.site.register(CommunityMembership)
admin.site.register(PostCommunity)
