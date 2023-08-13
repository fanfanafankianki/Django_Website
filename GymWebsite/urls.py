"""
URL configuration for GymWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Website_training_objects.views import return_all_profiles
from Website_training_objects.views import return_all_trainings
from Website_training_objects.views import return_all_exercises
from Website_training_objects.views import return_all_training_dates
from Website_training_objects.views import return_all_training_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('templates/profiles/', return_all_profiles),
    path('templates/trainings/', return_all_trainings),
    path('templates/exercises/', return_all_exercises),
    path('templates/training_dates/', return_all_training_dates),
    path('templates/training_details/', return_all_training_details),
]
