from django.db import models
from customers.models import Customer
from cars.models import Car

class Delivery(models.Model):

    STATUS_CHOICES = (

        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),

    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    delivery_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.customer.name