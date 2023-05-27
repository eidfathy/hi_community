from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile, PlacesProfile, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from posts.models import Post


class RegisterUserForm(UserCreationForm):
    CHOICES = [
        ('user_profile', 'user_profile'),
        ('places_profile', 'places_profile'),
    ]
    role = forms.ChoiceField(choices=CHOICES, initial='user_profile', widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2','role']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'birth_day', 'type', 'address', 'country', 'area', 'education', 'job_tite', 'about_me', 'interest']


class RegisterPlacesForm(UserCreationForm):
    CHOICES = [
        ('user_profile', 'user_profile'),
        ('places_profile', 'places_profile'),
    ]
    role = forms.ChoiceField(choices=CHOICES, initial='places_profile', widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','role']

class PlacesProfileForm(forms.ModelForm):
    class Meta:
        model = PlacesProfile
        fields = ['nameplaces', 'phone_number', 'type', 'address', 'country', 'area', 'sarves', 'about_me','facebook', 'instagram']



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required":"",
            "class": "input-email input",
            "name": "email",
            "id":"email",
            "placeholder": "Email",
            "type": "email",
            "required": "required",
            "placeholder":"Username",
        })
        self.fields["password"].widget.attrs.update({
            "class": "input-password input",
            "name": "password",
            "id":"password",
            "placeholder": "password",
            "type": "password",
            "required": "required",
            "placeholder":"Password",
        })


    username = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

INPUT_CLASSES = 'createPost bg-white rounded-3 p-4 mb-3'
class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.fields['description'].widget.attrs.update({
            'type':'text',
            'class':'form-control rounded-pill',
            'id':'CreatePost',
            'placeholder':'Some Something',
            'name':'description',
            'required':'',
        })
        self.fields['image'].widget.attrs.update({
            'type':'file',
            'id':'image',
            'name':'image',
        })
    class Meta:
        model = Post
        fields = ['description', 'image']
        widgets = {
            'description': forms.Select(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES})
        }
    description = forms.CharField(label='CreatePost', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control rounded-pill'}))

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


