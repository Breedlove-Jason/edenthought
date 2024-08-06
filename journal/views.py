from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import (
    CreateUserForm,
    LoginForm,
    ThoughtForm,
    UpdateUserForm,
    UpdateProfileForm,
)
from .models import Thought, Profile
from django.core.mail import send_mail
from django.conf import settings


def homepage(request):
    return render(request, "journal/index.html")


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            send_mail(
                "Welcome to Edenthought",
                """
            Hello,
                We're excited to have you join our community!
                Explore all the features we have to offer and feel free to get in touch with any inquiries you may have. We're here to help and make sure your experience with us is nothing short of excellent.
                Keep an eye on your inbox for tips, tricks, and the latest updates from us!
                Happy exploring!
            """,
                settings.EMAIL_HOST_USER,
                [current_user.email],
            )
            profile = Profile.objects.create(user=current_user)
            messages.success(
                request, "User created... " + form.cleaned_data.get("username")
            )
            return redirect("my-login")
    context = {"RegistrationForm": form}
    return render(request, "journal/register.html", context)


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    context = {"LoginForm": form}
    return render(request, "journal/my-login.html", context)


def user_logout(request):
    logout(request)
    return render(request, "journal/index.html")


@login_required(login_url="my-login")
def dashboard(request):
    profile_pic, created = Profile.objects.get_or_create(user=request.user)
    context = {"profilePic": profile_pic}
    return render(request, "journal/dashboard.html", context)


@login_required(login_url="my-login")
def create_thought(request):
    form = ThoughtForm()
    if request.method == "POST":
        form = ThoughtForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user  # Correctly set the user field
            thought.save()
            return redirect("my-thoughts")
    context = {"CreateThoughtForm": form}
    return render(request, "journal/create-thought.html", context)


@login_required(login_url="my-login")
def my_thoughts(request):
    current_user = request.user.id
    thought = Thought.objects.all().filter(user=current_user)
    context = {"AllThoughts": thought}
    return render(request, "journal/my-thoughts.html", context)


@login_required(login_url="my-login")
def update_thought(request, pk):
    try:
        thought = Thought.objects.get(id=pk, user=request.user)
    except:
        return redirect("my-thoughts")
    form = ThoughtForm(instance=thought)
    if request.method == "POST":
        form = ThoughtForm(request.POST, instance=thought)
        if form.is_valid():
            form.save()
            return redirect("my-thoughts")
    context = {"UpdateThought": form}
    return render(request, "journal/update-thought.html", context)


@login_required(login_url="my-login")
def delete_thought(request, pk):
    try:
        thought = Thought.objects.get(id=pk, user=request.user)
    except:
        return redirect("my-thoughts")
    if request.method == "POST":
        thought.delete()
        return redirect("my-thoughts")
    return render(request, "journal/delete-thought.html")


@login_required(login_url="my-login")
def profile_management(request):
    form = UpdateUserForm(instance=request.user)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"UserUpdateForm": form}
    return render(request, "journal/profile-management.html", context)


@login_required(login_url="my-login")
def upload_profile_pic(request):
    profile = Profile.objects.get(user=request.user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # messages.success(request, "Profile picture updated successfully")
            return redirect("dashboard")
    context = {"ProfileUpdateForm": form}
    return render(request, "journal/upload-profile-pic.html", context)


@login_required(login_url="my-login")
def delete_account(request):
    if request.method == "POST":
        delete_user = User.objects.get(username=request.user)
        delete_user.delete()
        return redirect("")
    return render(request, "journal/delete-account.html")
