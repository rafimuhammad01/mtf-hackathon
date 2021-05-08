from django.db import models

# Create your models here.

from JWTAuth.models import Employee


class BalanceHistory (models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=50)
    balance = models.FloatField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self) :
        return self.description


