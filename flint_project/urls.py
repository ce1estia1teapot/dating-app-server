"""
URL configuration for flint_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include API URLs from each app
    path('api/users/', include('users.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/matching/', include('matching.urls')),
    path('api/chat/', include('chat.urls')),
]
