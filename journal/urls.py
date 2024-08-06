from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page
    path("", views.homepage, name=""),
    # User registration
    path("register/", views.register, name="register"),
    # User login
    path("my-login/", views.my_login, name="my-login"),
    # User dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    # User logout
    path("user-logout/", views.user_logout, name="user-logout"),
    # Create a new thought
    path("create-thought/", views.create_thought, name="create-thought"),
    # View user's thoughts
    path("my-thoughts/", views.my_thoughts, name="my-thoughts"),
    # Update an existing thought
    path("update-thought/<int:pk>/", views.update_thought, name="update-thought"),
    # Delete an existing thought
    path("delete-thought/<int:pk>/", views.delete_thought, name="delete-thought"),
    # Profile management
    path("profile-management/", views.profile_management, name="profile-management"),
    # Delete user account
    path("delete-account/", views.delete_account, name="delete-account"),
    # Upload profile picture
    path("upload-profile-pic/", views.upload_profile_pic, name="upload-profile-pic"),
    # Password reset views
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="journal/password-reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent",
        auth_views.PasswordResetDoneView.as_view(template_name="journal/password-reset-sent.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="journal/password-reset-form.html"),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="journal/password-reset-complete.html"),
        name="password_reset_complete",
    ),
]