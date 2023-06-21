from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile, PlacesProfile, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from posts.models import Post



# class RegisterUserForm(UserCreationForm):
#     CHOICES = [
#         ('user_profile', 'user_profile'),
#         ('places_profile', 'places_profile'),
#     ]
#     role = forms.ChoiceField(choices=CHOICES, initial='user_profile', widget=forms.HiddenInput())
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__( *args, **kwargs)
#         self.fields["username"].widget.attrs.update({
#             "required":"",
#             "class": "input",
#             "name": "username",
#             "id":"username",
#             "placeholder": "username",
#             "type": "text",
#         })
#         self.fields["email"].widget.attrs.update({
#             "required":"",
#             "class": "input",
#             "name": "email",
#             "id":"email",
#             "placeholder": "email",
#             "type": "email",
#         })
#         self.fields["first_name"].widget.attrs.update({
#             "required":"",
#             "class": "input",
#             "name": "first_name",
#             "id":"first_name",
#             "placeholder": "first name",
#             "type": "text",
#         })
#         self.fields["last_name"].widget.attrs.update({
#             "required":"",
#             "class": "input",
#             "name": "last_name",
#             "id":"last_name",
#             "placeholder": "last name",
#             "type": "text",
#         })
#         self.fields["password1"].widget.attrs.update({
#             "required":"",
#             "class": "input",
#             "name": "password",
#             "id":"password",
#             "placeholder": "password",
#             "type": "password",
#         })
#         self.fields["password2"].widget.attrs.update({
#             "required":"",
#             "class": "input",
#             "name": "password",
#             "id":"password",
#             "placeholder": "password",
#             "type": "password",
#         })

#     class Meta:
#         model = User
#         fields = ['username', 'email','first_name','last_name', 'password1', 'password2','role']

class RegisterUserForm(UserCreationForm):
    CHOICES = [
        ('user_profile', 'user_profile'),
        ('places_profile', 'places_profile'),
    ]
    role = forms.ChoiceField(choices=CHOICES, initial='user_profile', widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2','role']

# class UserProfileForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs) -> None:
#             super().__init__( *args, **kwargs)
#             self.fields["phone_number"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "phone",
#                 "id":"phone",
#                 "placeholder": "phone number",
#                 "type": "tel",
#             })
#             self.fields["birth_day"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "date",
#                 "id":"date",
#                 "placeholder": "Date of birth",
#                 "type": "date",
#             })
#             self.fields["type"].widget.attrs.update({
#                 "required":"",
#                 "class": "input drop",
#                 "name": "gender",
#                 "id":"gender",
#                 "placeholder": "gender",
#                 "type": "text",
#             })
#             self.fields["address"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "address",
#                 "id":"address",
#                 "placeholder": "address",
#                 "type": "text",
#             })
#             self.fields["country"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "country",
#                 "id":"country",
#                 "placeholder": "country",
#                 "type": "text",
#             })
#             self.fields["area"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "area",
#                 "id":"area",
#                 "placeholder": "area",
#                 "type": "text",
#             })
#             self.fields["education"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "education",
#                 "id":"education",
#                 "placeholder": "education",
#                 "type": "text",
#             })
#             self.fields["job_tite"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "job_tite",
#                 "id":"job_tite",
#                 "placeholder": "job tite",
#                 "type": "text",
#             })
#             self.fields["interest"].widget.attrs.update({
#                 "required":"",
#                 "class": "input",
#                 "name": "interest",
#                 "id":"interest",
#                 "placeholder": "interest",
#                 "type": "text",
#             })
#     class Meta:
#         model = UserProfile
#         fields = ['phone_number', 'birth_day', 'type', 'address', 'country', 'area', 'education', 'job_tite', 'about_me', 'interest']

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


