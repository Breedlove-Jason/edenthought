from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import Thought


class ThoughtForm(ModelForm):
    class Meta:
        model = Thought
        fields = ["title", "content"]

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
