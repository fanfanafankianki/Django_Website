from django.shortcuts import render
from django.http import HttpResponse
from .models import Films

# Create your views here.
def wszystkie_filmy(request):
    test=Films.objects.all()
    return render(request, "filmy.html", {'filmy': test})