from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class DailyView(TemplateView):

    template_name = "main/daily.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["weekends_thismonth"] = self.get_weekends_month(0)
    #     context["weekends_nextmonth"] = self.get_weekends_month(1)
    #     return context

    