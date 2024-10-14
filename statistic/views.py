from django.shortcuts import render
from django.db.models import Sum
from .models import RoomBooking, FoodSale, CarRental
from django.utils import timezone
import calendar

def revenue_statistics(request):
    current_year = timezone.now().year
    selected_year = request.GET.get('year', current_year)

    room_revenue = RoomBooking.objects.filter(date_booked__year=selected_year).values('date_booked__month').annotate(total=Sum('amount')).order_by('date_booked__month')
    food_revenue = FoodSale.objects.filter(date_sold__year=selected_year).values('date_sold__month').annotate(total=Sum('amount')).order_by('date_sold__month')
    car_revenue = CarRental.objects.filter(date_rented__year=selected_year).values('date_rented__month').annotate(total=Sum('amount')).order_by('date_rented__month')

    monthly_room_revenue = [0] * 12
    monthly_food_revenue = [0] * 12
    monthly_car_revenue = [0] * 12

    for entry in room_revenue:
        monthly_room_revenue[entry['date_booked__month'] - 1] = entry['total']

    for entry in food_revenue:
        monthly_food_revenue[entry['date_sold__month'] - 1] = entry['total']

    for entry in car_revenue:
        monthly_car_revenue[entry['date_rented__month'] - 1] = entry['total']

    years = range(current_year - 5, current_year + 1)

    context = {
        'monthly_room_revenue': monthly_room_revenue,
        'monthly_food_revenue': monthly_food_revenue,
        'monthly_car_revenue': monthly_car_revenue,
        'months': list(calendar.month_name)[1:],
        'selected_year': selected_year,
        'years': years,
    }
    return render(request, 'statistic/revenue_statistics.html', context)
