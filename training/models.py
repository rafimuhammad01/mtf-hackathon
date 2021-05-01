from cloudinary.models import CloudinaryField
from django.db import models
from JWTAuth.models import Employee

# Create your models here.


class Training(models.Model):
    name = models.CharField(max_length=50)
    img = CloudinaryField('image')

    def __str__(self) :
        return self.name

class TrainingOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.owner) + str(self.training)

class Schedule(models.Model) :
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    training = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title