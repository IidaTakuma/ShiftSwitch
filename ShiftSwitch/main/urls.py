from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('',views.CalendarView.as_view(), name="calender"),
    path('daily/',views.DailyView.as_view(), name="daily"),
]