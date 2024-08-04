from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm


def homepage(request):
    return render(request, "journal/index.html")


def register(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
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


def dashboard(request):
    return render(request, "journal/dashboard.html")
