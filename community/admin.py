from django.contrib import admin
from .models import Community, CommunityMembership, PostCommunity, InterestCommunity


admin.site.register(Community)
admin.site.register(CommunityMembership)
admin.site.register(PostCommunity)
admin.site.register(InterestCommunity)
