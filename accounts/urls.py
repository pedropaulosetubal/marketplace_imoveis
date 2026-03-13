from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.shortcuts import redirect

from . import views
from .forms import UserCreationForm
from .models import User

app_name = "accounts"
urlpatterns = [
    path(
        "entrar/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "sair/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "cadastro/",
        CreateView.as_view(
            model=User,
            form_class=UserCreationForm,
            template_name="accounts/signup.html",
            success_url="/contas/entrar/",
        ),
        name="signup",
    ),
]
