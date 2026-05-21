from django.db import models


class Car(models.Model):

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    mileage = models.CharField(max_length=50)

    image = models.ImageField(upload_to='cars/')

    def __str__(self):

        return self.name