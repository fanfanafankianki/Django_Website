from django.forms import ModelForm
from .models import UserProfile, Exercise, Training, TrainingWithExercises, TrainingHistory, TrainingDetails

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_name']

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_name', 'exercise_image']

class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ['training_name', 'profile']

class TrainingWithExercisesForm(ModelForm):
    class Meta:
        model = TrainingWithExercises
        fields = ["training", "exercise_1", "exercise_2", "exercise_3", "exercise_4", "exercise_5", "exercise_6",
                    "exercise_7", "exercise_8", "exercise_9"]

class TrainingHistoryForm(ModelForm):
    class Meta:
        model = TrainingHistory
        fields = ["training_with_exercises", "training_date"]

class TrainingDetailsForm(ModelForm):
    class Meta:
        model = TrainingDetails
        fields = ["training_history", "exercise", "weight", "reps"]
