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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required": "required",
            "autofocus": "autofocus",
            "class": "input",
            "placeholder": "Username",
            "type": "text",
        })
        self.fields["email"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Email",
            "type": "email",
        })
        self.fields["first_name"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "First Name",
            "type": "text",
        })
        self.fields["last_name"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Last Name",
            "type": "text",
        })
        self.fields["password1"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Password",
            "type": "password",
        })
        self.fields["password2"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Confirm Password",
            "type": "password",
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role']
        labels = {
            "username": "",
            "email":"",
            "first_name":"",
            "last_name":"",
            "password1":"",
            "password2":"",
            "role":"",
        }


# class RegisterUserForm(UserCreationForm):
#     CHOICES = [
#         ('user_profile', 'user_profile'),
#         ('places_profile', 'places_profile'),
#     ]
#     role = forms.ChoiceField(choices=CHOICES, initial='user_profile', widget=forms.HiddenInput())
#     class Meta:
#         model = User
#         fields = ['username', 'email','first_name','last_name', 'password1', 'password2','role']

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone_number"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "phone",
            "id": "phone",
            "placeholder": "Phone Number",
            "type": "tel",
        })
        self.fields["birth_day"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "date",
            "id": "date",
            "placeholder": "Date of Birth",
            "type": "date",
        })
        self.fields["type"].widget.attrs.update({
            "required": "required",
            "class": "input drop",
            "name": "gender",
            "id": "gender",
            "placeholder": "Gender",
            "type": "text",
        })
        self.fields["address"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "address",
            "id": "address",
            "placeholder": "Address",
            "type": "text",
        })
        self.fields["country"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "country",
            "id": "country",
            "placeholder": "Country",
            "type": "text",
        })
        self.fields["area"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "area",
            "id": "area",
            "placeholder": "Area",
            "type": "text",
        })
        self.fields["education"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "education",
            "id": "education",
            "placeholder": "Education",
            "type": "text",
        })
        self.fields["job_tite"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "job_tite",
            "id": "job_tite",
            "placeholder": "Job Title",
            "type": "text",
        })
        self.fields["interest"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "interest",
            "id": "interest",
            "placeholder": "Interest",
            "type": "text",
        })
        self.fields["about_me"].widget.attrs.update({
            "required": "required",
            "class": "text-area input",
            "name": "email",
            "id": "email",
            "placeholder": "About you",
            "type": "text",
        })

    class Meta:
        model = UserProfile
        fields = [ "phone_number", "birth_day", "type", "address", "country", "area", "education", "job_tite", 'about_me',"interest"]
        labels = {
            "phone_number": "",
            "birth_day":"",
            "type":"",
            "address":"",
            "country":"",
            "area":"",
            "education":"",
            "job_tite":"",
            "about_me":"",
            "interest":"",
        }


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['phone_number', 'birth_day', 'type', 'address', 'country', 'area', 'education', 'job_tite', 'about_me', 'interest']


class RegisterPlacesForm(UserCreationForm):
    CHOICES = [
        ('user_profile', 'user_profile'),
        ('places_profile', 'places_profile'),
    ]
    role = forms.ChoiceField(choices=CHOICES, initial='places_profile', widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required": "required",
            "autofocus": "autofocus",
            "class": "input",
            "placeholder": "Username",
            "type": "text",
        })
        self.fields["email"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Email",
            "type": "email",
        })
        self.fields["first_name"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "First Name",
            "type": "text",
        })
        self.fields["last_name"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Last Name",
            "type": "text",
        })
        self.fields["password1"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Password",
            "type": "password",
        })
        self.fields["password2"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "placeholder": "Confirm Password",
            "type": "password",
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role']
        labels = {
            "username": "",
            "email":"",
            "first_name":"",
            "last_name":"",
            "password1":"",
            "password2":"",
            "role":"",
        }

class PlacesProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nameplaces"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "place name",
            "id": "place name",
            "placeholder": "Name of the place",
            "type": "text",
        })
        self.fields["phone_number"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "phone",
            "id": "phone",
            "placeholder": "Phone Number",
            "type": "tel",
        })
        self.fields["type"].widget.attrs.update({
            "required": "required",
            "class": "input drop",
            "name": "gender",
            "id": "gender",
            "placeholder": "Gender",
            "type": "text",
        })
        self.fields["address"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "address",
            "id": "address",
            "placeholder": "Address",
            "type": "text",
        })
        self.fields["country"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "country",
            "id": "country",
            "placeholder": "Country",
            "type": "text",
        })
        self.fields["area"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "area",
            "id": "area",
            "placeholder": "Area",
            "type": "text",
        })
        self.fields["sarves"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "sevices",
            "id": "sevices",
            "placeholder": "Services",
            "type": "text",
        })
        self.fields["about_me"].widget.attrs.update({
            "required": "required",
            "class": "text-area input",
            "name": "message",
            "id": "message",
            "rows":"5",
            "placeholder": "About you",
            "type": "text",
        })
        self.fields["facebook"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "facebook",
            "id": "facebook",
            "placeholder": "Facebook Link",
            "type": "text",
        })
        self.fields["instagram"].widget.attrs.update({
            "required": "required",
            "class": "input",
            "name": "instagram",
            "id": "instagram",
            "placeholder": "Inistagram Link",
            "type": "text",
        })

    class Meta:
        model = PlacesProfile
        fields = ['nameplaces', 'phone_number', 'type', 'address', 'country', 'area', 'sarves', 'about_me','facebook', 'instagram']
        labels = {
            "nameplaces": "",
            "phone_number":"",
            "type":"",
            "last_name":"",
            "address":"",
            "country":"",
            "area":"",
            "sarves":"",
            "about_me":"",
            "facebook":"",
            "instagram":"",
        }



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


