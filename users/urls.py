from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import urls
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"
"""
configuring urls to the view functions
"""
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path("register", views.register, name="register"),
    path('info/<int:user_id>', views.info, name="info")
]
