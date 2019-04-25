from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('',views.CalendarView.as_view(), name="calender"),
    path('daily/',views.DailyView.as_view(), name="daily"),
    path('absence/create/',views.AbsenceCreateView.as_view(),name="absenceCreate"),
    path('absence/change/<int:pk>/',views.AbsenceChangeView.as_view(), name="absenceChange"),
    path('alternative/create/',views.AlternativeCreateView.as_view(), name="alternativeCreate"),
    path('alternative/change/<int:pk>/',views.AlternativeChangeView.as_view(), name="alternativeChange"),
]