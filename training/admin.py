from django.contrib import admin

# Register your models here.
from training.models import Training, Schedule, TrainingOwned, Competency

admin.site.register(Training)
admin.site.register(Schedule)
admin.site.register(TrainingOwned)
admin.site.register(Competency)