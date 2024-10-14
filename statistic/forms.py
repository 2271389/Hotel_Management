from django import forms
from .models import RoomBooking, FoodSale, CarRental

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['customer_name', 'date_booked', 'amount']

class FoodSaleForm(forms.ModelForm):
    class Meta:
        model = FoodSale
        fields = ['customer_name', 'date_sold', 'amount']

class CarRentalForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = ['customer_name', 'date_rented', 'amount']
