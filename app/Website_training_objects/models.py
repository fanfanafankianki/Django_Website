# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    profile_name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Profile Name: {self.profile_name}, User: {self.user}"

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=50)
    exercise_image = models.ImageField(upload_to="exercise_images", null=True, blank=True)

    def __str__(self):
        return self.exercise_name

class Training(models.Model):
    training_name = models.CharField(max_length=55)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Training Name: {self.training_name}, Profile: {self.profile.profile_name}"


class TrainingWithExercises(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)

    exercise_1 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_1_set")
    exercise_2 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_2_set")
    exercise_3 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_3_set")
    exercise_4 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_4_set", null=True,
                                   blank=True)
    exercise_5 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_5_set", null=True,
                                   blank=True)
    exercise_6 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_6_set", null=True,
                                   blank=True)
    exercise_7 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_7_set", null=True,
                                   blank=True)
    exercise_8 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_8_set", null=True,
                                   blank=True)
    exercise_9 = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise_9_set", null=True,
                                   blank=True)

    def __str__(self):
        exercises = [self.exercise_1, self.exercise_2, self.exercise_3, self.exercise_4, self.exercise_5,
                     self.exercise_6, self.exercise_7, self.exercise_8, self.exercise_9]
        exercises_str = ', '.join([exercise.exercise_name for exercise in exercises if exercise])
        return f"Training: {self.training.training_name}, Exercises: {exercises_str}"


class TrainingHistory(models.Model):
    training_with_exercises = models.ForeignKey(TrainingWithExercises, on_delete=models.CASCADE)
    training_date = models.DateTimeField(default=timezone.now)  # Ustawia domyślnie aktualną datę i czas

    def __str__(self):
        return f"History for training: {self.training_with_exercises.training.training_name} with exercises: {self.training_with_exercises} on {self.training_date}"

class TrainingDetails(models.Model):
    training_history = models.ForeignKey(TrainingHistory, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Details: Training History: {self.training_history}, Exercise: {self.exercise.exercise_name}, Weight: {self.weight}, Reps: {self.reps}"

class Testing(models.Model):
    name = models.CharField(max_length=55)
    imagePath = models.ImageField(upload_to="testing_images", null=True, blank=True)
    description = models.CharField(max_length=55)

    def __str__(self):
        return f"Name: {self.name}, image {self.imagePath}, description: {self.description}"