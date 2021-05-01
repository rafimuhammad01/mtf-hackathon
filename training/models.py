from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.db import models
from JWTAuth.models import Employee

# Create your models here.


class Training(models.Model):
    name = models.CharField(max_length=50)
    img = CloudinaryField('image')
    organizer = models.CharField(max_length=50)
    about = RichTextField(blank=True)


    def __str__(self) :
        return self.name

class TrainingOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.owner) + str(self.training)

class Schedule(models.Model) :
    ONLINE = 0
    OFFLINE = 1
    METHOD = [
        (ONLINE, "Online"),
        (OFFLINE, "Offline"),
    ]
    title = models.CharField(max_length=50)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    method = models.IntegerField(choices=METHOD, blank=True, null=True)
    linkUrl = models.URLField(blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) :
        return self.title