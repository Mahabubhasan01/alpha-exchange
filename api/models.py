import email
from django.db import models
from django.forms import CharField

# Create your models here.
payment_method = (
    ('Bkash', 'Bkash'), ('Nagad', 'Nagad'), ('Rocket', 'Rocket'), ('Upay', 'Upay'), ('Visa/Master card', 'Visa/Master card'),)


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    send_method = models.CharField(max_length=100, choices=payment_method)
    receive_method = models.CharField(max_length=100, choices=payment_method)
    send_amount = models.PositiveIntegerField()
    receive_amount = models.PositiveIntegerField()
    send_number = models.BigIntegerField()
    receive_number = models.BigIntegerField()
    contact_number = models.IntegerField()

    def __str__(self) -> str:
        return self.name
