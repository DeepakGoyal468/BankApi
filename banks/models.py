from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    ifsc_code = models.CharField(max_length=100, unique=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ifsc_code