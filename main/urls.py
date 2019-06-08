from django.urls import path
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('absence/create/',views.AbsenceCreateView.as_view(),name="absenceCreate"),
    path('absence/delete/<int:pk>/',views.DeleteAbsenceView.as_view(), name="deleteAbsence"),
    path('alternative/create/',views.AlternativeCreateView.as_view(), name="alternativeCreate"),
    path('alternative/delete/<int:pk>/',views.DeleteAlternativeView.as_view(), name="deleteAlternative"),
    path('',views.CalendarView.as_view(), name="calender"),
    path('daily/',views.DailyView.as_view(), name="daily"),
    path('mypage/',views.MyPageView.as_view(), name="mypage"),
    path('mypage/edit/<int:pk>/',views.MyPageEditView.as_view(), name="mypageEdit"),
    path('manager/calender/',views.ManagerCalenderView.as_view(), name="managerCalender"),
    path('manager/daily/',views.ManagerDailyView.as_view(), name="managerDaily"),
]