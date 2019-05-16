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
        is_absence = Absence.objects.filter(date=_date).filter(is_settled=False).count()
        is_alternative = Alternative.objects.filter(date=_date).filter(is_settled=False).count()
        context["deficiency"] = is_alternative - is_absence
        #過不足を渡す部分[終了]

        context['absence_changed_list'] = Absence.objects.filter(date = _date).filter(is_settled = True)
        context['alternative_changed_list'] = Alternative.objects.filter(date = _date).filter(is_settled = True)
        context['absence_not_changed_list'] = Absence.objects.filter(date=_date).filter(is_settled = False)
        context['alternative_not_changed_list'] = Alternative.objects.filter(date=_date).filter(is_settled = False)

        return context

