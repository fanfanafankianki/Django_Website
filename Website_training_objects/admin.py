from django.contrib import admin
from .models import UserProfile, Exercise, Training, TrainingWithExercises, TrainingHistory, TrainingDetails

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["profile_name", "user"]
    list_filter = ("user",)
    search_fields = ("user",)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["exercise_name", "exercise_image"]
    list_filter = ("exercise_name",)

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ["training_name", "profile"]
    list_filter = ("profile",)
    search_fields = ("profile",)

@admin.register(TrainingWithExercises)
class TrainingWithExercisesAdmin(admin.ModelAdmin):
    list_display = ["training", "exercise_1", "exercise_2", "exercise_3", "exercise_4", "exercise_5", "exercise_6",
                    "exercise_7", "exercise_8", "exercise_9"]
    list_filter = ("training",)
    search_fields = ("training",)

@admin.register(TrainingHistory)
class TrainingHistoryAdmin(admin.ModelAdmin):
    list_display = ["training_with_exercises", "training_date"]
    list_filter = ("training_with_exercises",)

@admin.register(TrainingDetails)
class TrainingDetailsAdmin(admin.ModelAdmin):
    list_display = ["training_history", "exercise", "weight", "reps"]
    list_filter = ("exercise",)