from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import UserProfile, Exercise, Training, TrainingWithExercises, TrainingHistory, TrainingDetails
from .forms import UserProfileForm, ExerciseForm, TrainingForm, TrainingWithExercisesForm, TrainingHistoryForm, TrainingDetailsForm

#Profile
def return_user_profile(request, id):
    user_profiles = UserProfile.objects.filter(id=id)
    return render(request, "profile_info/profile.html", {'user_profiles': user_profiles})

def create_user_profile(request):
    create_form = UserProfileForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "profile_info/profile_new.html", {'profile_new': create_form})

def edit_user_profile(request, id):
    profile = get_object_or_404(UserProfile, pk=id)
    edit_form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "profile_info/profile_new.html", {'profile_new': edit_form})

def delete_user_profile(request, id):
    instance_object = get_object_or_404(UserProfile, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "profile_info/profile_delete.html", {'profile_delete': instance_object})

#Exercises
def return_all_exercises(request):
    exercises = Exercise.objects.all()
    return render(request, "profile_info/exercises.html", {'exercises': exercises})

def return_exercises(request, id):
    exercises = Exercise.objects.filter(id=id)
    return render(request, "profile_info/exercises.html", {'exercises': exercises})

def create_exercises(request):
    create_form = ExerciseForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "profile_info/exercises_new.html", {'exercise_new': create_form})

def edit_exercises(request, id):
    instance_object = get_object_or_404(Exercise, pk=id)
    edit_form = ExerciseForm(request.POST or None, request.FILES or None, instance=instance_object)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "profile_info/exercises_new.html", {'exercise_new': edit_form})

def delete_exercises(request, id):
    exercise = get_object_or_404(Exercise, pk=id)

    if request.method == "POST":
        exercise.delete()
        return redirect(new_profile)

    return render(request, "profile_info/exercises_delete.html", {'exercise_delete': exercise})


#Trainings
def return_all_trainings(request):
    trainings = Training.objects.all()
    return render(request, "profile_info/training_instance.html", {'trainings': trainings})

def return_training(request, id):
    trainings = Training.objects.filter(id=id)
    return render(request, "profile_info/training_instance.html", {'trainings': trainings})

def create_training(request):
    create_form = TrainingForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "profile_info/training_instance_new.html", {'training_new': create_form})

def edit_training(request, id):
    instance_object = get_object_or_404(Training, pk=id)
    edit_form = TrainingForm(request.POST or None, request.FILES or None, instance=instance_object)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "profile_info/training_instance_new.html", {'training_new': edit_form})

def delete_training(request, id):
    instance_object = get_object_or_404(Training, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "profile_info/training_instance_delete.html", {'training_delete': instance_object})

#Trainings_with_exercises
def return_all_training_with_exercises(request):
    training_with_exercises = TrainingWithExercises.objects.all()
    return render(request, "profile_info/training_with_exercises.html", {'training_with_exercises': training_with_exercises})

def return_training_with_exercises(request, id):
    training_with_exercises = TrainingWithExercises.objects.filter(id=id)
    return render(request, "profile_info/training_with_exercises.html", {'training_with_exercises': training_with_exercises})

def create_training_with_exercises(request):
    create_form = TrainingWithExercisesForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "profile_info/training_with_exercises_new.html", {'training_with_exercises_new': create_form})

def edit_training_with_exercises(request, id):
    instance_object = get_object_or_404(TrainingWithExercises, pk=id)
    edit_form = TrainingWithExercisesForm(request.POST or None, request.FILES or None, instance=instance_object)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "profile_info/training_with_exercises_new.html", {'training_with_exercises_new': edit_form})

def delete_training_with_exercises(request, id):
    instance_object = get_object_or_404(TrainingWithExercises, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "profile_info/training_with_exercises_delete.html", {'training_with_exercises_delete': instance_object})


#Training_history
def return_all_training_history(request):
    training_histories = TrainingHistory.objects.all()
    return render(request, "profile_info/training_history.html", {'training_histories': training_histories})

def return_training_history(request, id):
    training_history = TrainingHistory.objects.filter(id=id)
    return render(request, "profile_info/training_history.html", {'training_history': training_history})

def create_training_history(request):
    create_form = TrainingHistoryForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "profile_info/training_history_new.html", {'training_history_new': create_form})

def edit_training_history(request, id):
    instance_object = get_object_or_404(TrainingHistory, pk=id)
    edit_form = TrainingHistoryForm(request.POST or None, request.FILES or None, instance=instance_object)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "profile_info/training_history_new.html", {'training_history_new': edit_form})

def delete_training_history(request, id):
    instance_object = get_object_or_404(TrainingHistory, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "profile_info/training_history_delete.html", {'training_history_delete': instance_object})

#TrainingDetails
def return_all_training_details(request):
    training_details = TrainingDetails.objects.all()
    return render(request, "profile_info/training_details.html", {'training_details': training_details})

def return_training_details(request, id):
    training_details = TrainingDetails.objects.filter(id=id)
    return render(request, "profile_info/training_details.html", {'training_details': training_details})

def create_training_details(request):
    create_form = TrainingDetailsForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "profile_info/training_details_new.html", {'training_details_new': create_form})

def edit_training_details(request, id):
    instance_object = get_object_or_404(TrainingDetails, pk=id)
    edit_form = TrainingHistoryForm(request.POST or None, request.FILES or None, instance=instance_object)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "profile_info/training_details_new.html", {'training_details_new': edit_form})

def delete_training_details(request, id):
    instance_object = get_object_or_404(TrainingDetails, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "profile_info/training_details_delete.html", {'training_details_delete': instance_object})

