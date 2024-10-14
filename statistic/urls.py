from django.urls import path
from .views import revenue_statistics

urlpatterns = [
    path('revenue/', revenue_statistics, name='revenue_statistics'),
]
