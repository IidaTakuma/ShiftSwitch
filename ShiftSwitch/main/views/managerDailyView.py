from django.views.generic import TemplateView
from main.models import Absence, Alternative
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class ManagerDailyView(LoginRequiredMixin,TemplateView):
    template_name = 'main/managerDaily.html'
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.request.GET.get('y')
        month = self.request.GET.get('m')
        day = self.request.GET.get('d')
        week = self.request.GET.get('w')

        context["year"] = year
        context["month"] = month
        context["day"] = day
        context["week"] = week

        _date = str(year) + "-" + str(month) + "-" + str(day)
        context['absence_changed_list'] = Absence.objects.filter(date = _date).filter(is_settled = True)
        context['alternative_changed_list'] = Alternative.objects.filter(date = _date).filter(is_settled = True)
        context['absence_not_changed_list'] = Absence.objects.filter(date=_date).filter(is_settled = False)
        context['alternative_not_changed_list'] = Alternative.objects.filter(date=_date).filter(is_settled = False)

        return context

