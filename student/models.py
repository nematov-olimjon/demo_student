from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('')
