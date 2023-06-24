from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from .models import Community
from .forms import CommunityForm

@login_required
def community(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    community_list = Community.objects.all()
    created_communities = Community.objects.filter(creator=profile)
    context = {
        'profile': profile,
        'communitys': community_list,
        'mycommunity':created_communities
    }
    return render(request, 'community.html', context)

@login_required
def community_profile(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    context = {'community': community}
    return render(request, 'community_profile.html', context)


def create_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.creator = request.user
            community.save()
            community.members.add(request.user)
            return redirect('community_profile', community_id=community.id)
    else:
        form = CommunityForm()
    
    context = {'form': form}
    return render(request, 'create_community.html', context)


