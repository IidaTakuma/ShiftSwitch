from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('absence/create/',views.AbsenceCreateView.as_view(),name="absenceCreate"),
    path('absence/change/<int:pk>/',views.AbsenceChangeView.as_view(), name="absenceChange"),
    path('absence/delete/<int:pk>/',views.DeleteAbsenceView.as_view(), name="deleteAbsence"),
    path('alternative/create/',views.AlternativeCreateView.as_view(), name="alternativeCreate"),
    path('alternative/change/<int:pk>/',views.AlternativeChangeView.as_view(), name="alternativeChange"),
    path('alternative/delete/<int:pk>/',views.DeleteAlternativeView.as_view(), name="deleteAlternative"),
    path('',views.CalendarView.as_view(), name="calender"),
    path('daily/',views.DailyView.as_view(), name="daily"),
    path('mypage/',views.MyPageView.as_view(), name="mypage"),
    path('manager/calender/',views.ManagerCalenderView.as_view(), name="managerCalender"),
    path('manager/daily/',views.ManagerDailyView.as_view(), name="managerDaily"),
]