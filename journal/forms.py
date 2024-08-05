from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput

from .models import Thought, Profile


class ThoughtForm(ModelForm):
    class Meta:
        model = Thought
        fields = ["title", "content"]
        exclude = ["user"]

        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "content": TextInput(
                attrs={"class": "form-control", "placeholder": "Content"}
            ),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "email": TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "password1": PasswordInput(
                attrs={"class": "form-control", "placeholder": "Password"}
            ),
            "password2": PasswordInput(
                attrs={"class": "form-control", "placeholder": "Confirm Password"}
            ),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )


class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]
        exclude = [
            "password1",
            "password2",
        ]

        widgets = {
            "username": TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "email": TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
        }


class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control-file"})
    )

    class Meta:
        model = Profile
        fields = ("profile_pic",)
