from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Absence, Alternative
from .methods import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class DailyView(LoginRequiredMixin,TemplateView):
    model = Absence
    template_name = "main/daily.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_dateData_to_context(self, context)
        _date = get_date(self)
        #過不足を渡す部分[開始]
        is_absence = Absence.objects.filter(date=_date,is_settled=False).count()
        is_alternative = Alternative.objects.filter(date=_date,is_settled=False).count()
        context["deficiency"] = is_alternative - is_absence
        #過不足を渡す部分[終了]

        _user = self.request.user
        context['absence_list'] = Absence.objects.filter(date = _date).exclude(Absence_user = _user)
        context['alternative_list'] = Alternative.objects.filter(date = _date).exclude(Alternative_user = _user)
        context['ownAbsence'] = Absence.objects.filter(date = _date, Absence_user = _user)
        context['ownAlternative'] = Alternative.objects.filter(date = _date, Alternative_user = _user)

        context['ownAbsenceChange'] = Absence.objects.filter(date = _date, Alternative_user = _user.id)
        context['ownAlternativeChange'] = Alternative.objects.filter(date = _date, Absence_user = _user.id)

        return context
