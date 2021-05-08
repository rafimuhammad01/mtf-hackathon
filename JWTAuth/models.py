from datetime import datetime

from cloudinary.models import CloudinaryField
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

    MALE = 0
    FEMALE = 1
    SEX_TYPES = [
        (MALE, "MALE"),
        (FEMALE, "FEMALE")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = CloudinaryField('image', null=True, blank=True)
    pewiraMilesBalance = models.FloatField(default=0)
    status = models.IntegerField(default=STAFF, choices=EMPLOYEE_TYPES)
    posistion = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    start_work_date = models.DateTimeField(default=datetime.now())
    sex = models.IntegerField(choices=SEX_TYPES)

    def __str__(self) :
        return self.user.username

