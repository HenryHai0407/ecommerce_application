# accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

# Create app_name
app_name = 'accounts'

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="products/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
]
