from django.db import models

# Create your models here.
class Profiles(models.Model):
    name = models.CharField(max_length=64)
    rok = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return self.tytul_z_rokiem()
    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)

class Training(models.Model):
    name = models.CharField(max_length=64)
    rok = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return self.tytul_z_rokiem()
    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)

class Exercise(models.Model):
    name = models.CharField(max_length=64)
    rok = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return self.tytul_z_rokiem()
    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)

class TrainingDate(models.Model):
    name = models.CharField(max_length=64)
    rok = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return self.tytul_z_rokiem()
    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)

class TrainingDetails(models.Model):
    name = models.CharField(max_length=64)
    rok = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return self.tytul_z_rokiem()
    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)