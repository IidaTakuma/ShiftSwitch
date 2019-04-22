from django.shortcuts import render
from django.views.generic import TemplateView

from datetime import date, timedelta
# Create your views here.

class CalendarView(TemplateView):

    template_name = "main/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weekends"] = self.get_weekends
        return context
    
    def get_weekends(self):
        this_month = date.today()

        end_day = (date(this_month.year, this_month.month+1, 1) - timedelta(days=1)).day

        weekend = []
        for day in range(1,int(end_day)+1):
            d = date(this_month.year, this_month.month, day)
            if d.weekday()==5:
                weekend.append((day,"Sat"))
            elif d.weekday()==6:
                weekend.append((day,"Sun"))
        
        return weekend