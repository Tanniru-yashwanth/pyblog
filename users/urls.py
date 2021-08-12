from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import urls
from . import views

app_name = "users"
"""
configuring urls to the view functions
"""
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", views.register, name="register"),
    path('info/<int:user_id>', views.info, name="info")
]
