from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class DailyView(TemplateView):

    template_name = "main/daily.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month = self.request.GET.get('m')
        day = self.request.GET.get('d')
        week = self.request.GET.get('w')

        context["month"] = month
        context["day"] = day
        context["week"] = week

        return context

    