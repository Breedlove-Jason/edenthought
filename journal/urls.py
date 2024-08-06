from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.homepage, name=""),
    path("register/", views.register, name="register"),
    path("my-login/", views.my_login, name="my-login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("user-logout/", views.user_logout, name="user-logout"),
    path("create-thought/", views.create_thought, name="create-thought"),
    path("my-thoughts/", views.my_thoughts, name="my-thoughts"),
    path("update-thought/<int:pk>/", views.update_thought, name="update-thought"),
    path("delete-thought/<int:pk>/", views.delete_thought, name="delete-thought"),
    path("profile-management/", views.profile_management, name="profile-management"),
    path("delete-account/", views.delete_account, name="delete-account"),
    path("upload-profile-pic/", views.upload_profile_pic, name="upload-profile-pic"),
    # Password management
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="reset"),
    path(
        "reset_password_sent",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
