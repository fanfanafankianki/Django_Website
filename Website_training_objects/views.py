from django.shortcuts import render
from django.http import HttpResponse
from .models import Profiles
from .models import Training
from .models import Exercise
from .models import TrainingDate
from .models import TrainingDetails

# Create your views here.
def return_all_profiles(request):
    test=Profiles.objects.all()
    return render(request, "filmy.html", {'filmy': test})

def return_all_trainings(request):
    test=Training.objects.all()
    return render(request, "filmy.html", {'filmy': test})

def return_all_exercises(request):
    test=Exercise.objects.all()
    return render(request, "filmy.html", {'filmy': test})

def return_all_training_dates(request):
    test=TrainingDate.objects.all()
    return render(request, "filmy.html", {'filmy': test})

def return_all_training_details(request):
    test=TrainingDetails.objects.all()
    return render(request, "filmy.html", {'filmy': test})
