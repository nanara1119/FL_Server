"""FL_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('admin/', admin.site.urls),
    path('round', views.round),
    path('client_count', views.client_count),
    path('client_count/', views.client_count),
    path('client_count/<int:count>', views.client_count),
    path('weight', views.weight),
    path('weight/', views.weight),
    path('reset', views.reset),
    path('reset/', views.reset),
    path('params', views.all_params),
    path('params/', views.all_params)
]
