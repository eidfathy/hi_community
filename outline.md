# accounts / views #

# @login_required
# def user_profile(request, profile_id):
#     profile = get_object_or_404(UserProfile, user=request.user, id=profile_id)
#     post_user_list = Post.objects.filter(creater=profile.user)
#     context = {'profile': profile, 'posts': post_user_list}
#     return render(request, 'profile_user.html', context)

# @login_required
# def create_post(request):
#     user = request.user.id
    
#     if request.method == 'POST':
#         form = NewPostForm(request.POST, request.FILES)

#         if form.is_valid():
#             image = form.cleaned_data.get('image')
#             description = form.cleaned_data.get('description')
            
#             p, created = Post.objects.get_or_create(image=image, description=description, user_id=user )
#             p.save()
            
#             return redirect('userprofile')
#     else:
#         form = NewPostForm()
        
#     context = {'form': form}
#     return render(request, 'profile_user.html', context)




# @login_required
# def home(request,):
#     profile = get_object_or_404(UserProfile, user=request.user)
#     post_user_list = Post.objects.all()
#     context = {'profile':profile, 'posts':post_user_list} # tempate name
#     return render(request, 'home.html', context)

# @login_required
# def home(request):
#     user = request.user
#     home = get_object_or_404(UserProfile, user=user)
#     context = {'home': home,}
#     return render(request, 'home.html', context)


# @login_required
# def home(request, home_id):
#     home = get_object_or_404(UserProfile, id=home_id, user=request.user)
#     context = {'home': home,}
#     return render(request, 'home.html', context)

# accounts / models #

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

# accounts / forms #

# class NewPostForm(forms.ModelForm):
#     description = forms.CharField(
#         label='CreatePost',
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control rounded-pill createPost bg-white rounded-3 p-4 mb-3'})
#     )

#     class Meta:
#         model = Post
#         fields = ['description', 'image']
#         widgets = {
#             'image': forms.FileInput(attrs={'class': 'createPost bg-white rounded-3 p-4 mb-3'})
#         }



# class NewPostForm(forms.ModelForm):
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control rounded-pill'}), required=True)
#     image = forms.ImageField(required=True)

#     class Meta:
#         model = Post
#         fields = ['description', 'image']

# vommunity #

# @login_required
# def community(request, profile_id):
#     profile = get_object_or_404(Community, user=request.user, id=profile_id)
#     context = {'profile': profile, }
#     return render(request, 'community.html', context)