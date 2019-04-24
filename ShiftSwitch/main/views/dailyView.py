from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Absence

# Create your views here.

class DailyView(TemplateView):
    model = Absence
    template_name = "main/daily.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.request.GET.get('y')
        month = self.request.GET.get('m')
        day = self.request.GET.get('d')
        week = self.request.GET.get('w')

        context["month"] = month
        context["day"] = day
        context["week"] = week

        _date = str(year) + "-" + str(month) + "-" + str(day)
        context['absence_list'] = Absence.objects.filter(date = _date)

        return context
