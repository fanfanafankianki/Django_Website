from django.contrib import admin
from .models import Profiles
from .models import Training
from .models import Exercise
from .models import TrainingDate
from .models import TrainingDetails
# Register your models here.

admin.site.register(Profiles)
admin.site.register(Training)
admin.site.register(Exercise)
admin.site.register(TrainingDate)
admin.site.register(TrainingDetails)