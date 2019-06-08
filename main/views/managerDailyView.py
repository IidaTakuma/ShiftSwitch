from django.views.generic import TemplateView
from main.models import Absence, Alternative
from users.models import User
from .methods import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ManagerDailyView(LoginRequiredMixin,TemplateView):
    template_name = 'main/managerDaily.html'
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_dateData_to_context(self, context)
        
        _date = get_date(self)

        #過不足を渡す部分[開始]
        is_absence = Absence.objects.filter(date=_date).count()
        is_alternative = Alternative.objects.filter(date=_date).count()
        context["deficiency"] = is_alternative - is_absence
        #過不足を渡す部分[終了]

        context['absenceList_AM'] = Absence.objects.filter(date = _date).filter(shift_zone = "AM")
        context['absenceList_PM'] = Absence.objects.filter(date = _date).filter(shift_zone = "PM")
        context['absenceList_BOTH'] = Absence.objects.filter(date = _date).filter(shift_zone = "BOTH")
        context['alternativeList_AM'] = Alternative.objects.filter(date = _date).filter(shift_zone = "AM")
        context['alternativeList_PM'] = Alternative.objects.filter(date = _date).filter(shift_zone = "PM")
        context['alternativeList_BOTH'] = Alternative.objects.filter(date = _date).filter(shift_zone = "BOTH")

        return context

