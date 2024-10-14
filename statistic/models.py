from django.db import models

class RoomBooking(models.Model):
    customer_name = models.CharField(max_length=100)
    date_booked = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class FoodSale(models.Model):
    customer_name = models.CharField(max_length=100)
    date_sold = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class CarRental(models.Model):
    customer_name = models.CharField(max_length=100)
    date_rented = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
