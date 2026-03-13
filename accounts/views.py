from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect

from .forms import UserCreationForm
from .models import User


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        return redirect("accounts:login")


urlpatterns_accounts = [
    ("login/", LoginView.as_view(template_name="accounts/login.html"), "login"),
    ("logout/", LogoutView.as_view(), "logout"),
    ("cadastro/", SignUpView.as_view(), "signup"),
]
