from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    STAFF = 0
    ADMIN = 1
    SUPERADMIN = 2
    EMPLOYEE_TYPES = [
        (STAFF, "Staff"),
        (ADMIN, "Admin"),
        (SUPERADMIN, "Super Admin")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #course = models.ManyToManyField('Course', blank=True)
    #training = models.ManyToManyField('Training', blank=True)
    pewiraMilesBalance = models.FloatField(default=0)
    status = models.IntegerField(default=STAFF, choices=EMPLOYEE_TYPES)

    def __str__(self) :
        return self.user.username

