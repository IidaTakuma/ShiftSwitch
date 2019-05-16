from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import date, timedelta
# Create your views here.

class CalendarView(LoginRequiredMixin,TemplateView):

    template_name = "main/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weekends_thismonth"] = self.get_weekends_month(0)
        context["weekends_nextmonth"] = self.get_weekends_month(1) 
        return context
    
    def get_weekends_month(self,flag):
        this_month = date.today()
        year = this_month.year
        month = this_month.month + flag
        if month == 12:
            end_day = 31
        elif month == 13:
            year = year + 1
            month = 12
            end_day = 31
        else:
            end_day = (date(year, month+1, 1) - timedelta(days=1)).day

        weekend = []
        for day in range(1,int(end_day)+1):
            d = date(year, month, day)
            if d.weekday()==5:
                weekend.append((year,month,day,"Sat"))
            elif d.weekday()==6:
                weekend.append((year,month,day,"Sun"))
        
        return weekend

    