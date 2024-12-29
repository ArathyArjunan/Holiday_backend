from django.urls import path
from .views import FetchHolidaysView

urlpatterns = [
    path('fetch/', FetchHolidaysView.as_view(), name='fetch_holidays'),
]
