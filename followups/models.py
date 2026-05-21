from django.db import models
from customers.models import Customer
from cars.models import Car


class Followup(models.Model):

    STATUS_CHOICES = (

        ('Pending', 'Pending'),
        ('Interested', 'Interested'),
        ('Booked', 'Booked'),
        ('No Response', 'No Response'),

    )

    customer = models.ForeignKey(Customer,
        on_delete=models.CASCADE)

    car = models.ForeignKey(Car,
        on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)

    followup_date = models.DateField()

    status = models.CharField(max_length=50,
        choices=STATUS_CHOICES)

    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.customer.name