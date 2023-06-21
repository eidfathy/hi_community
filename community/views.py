from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from .models import Community

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


# def create_community(request):
#     if request.method == 'POST':
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             group = form.save(commit=False)
#             group.creator = request.user
#             group.save()
#             group.members.add(request.user)
#             return redirect('group_detail', group_id=group.id)
#     else:
#         form = GroupForm()
    
#     context = {'form': form}
#     return render(request, 'create_community.html', context)

