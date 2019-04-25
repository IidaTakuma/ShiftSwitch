from django.shortcuts import render, redirect
from django.views.generic import CreateView
from main.models import Absence
from main.forms.absenceCreateForm import AbsenceCreateForm

class AbsenceCreateView(CreateView):
    model = Absence
    template_name = "main/absenceCreate.html"
    form_class = AbsenceCreateForm

    # fields = ("shift_zone", "comment",)

    def get_date(self):
        year = self.request.GET.get('y')
        month = self.request.GET.get('m')
        day = self.request.GET.get('d')
        _date = str(year) + "-" + str(month) + "-" + str(day)
        return _date

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month = self.request.GET.get('m')
        day = self.request.GET.get('d')
        week = self.request.GET.get('w')
        
        context["month"] = month
        context["day"] = day
        context["week"] = week

        return context

    def post(self, request, *args, **kwargs):

        _shift_zone = request.POST['shift_zone']
        _comment = request.POST['comment']
        
        absence = Absence()
        absence.shift_zone = _shift_zone
        absence.comment = _comment
        absence.Absence_user = request.user
        absence.date = self.get_date()
        absence.save()

        return redirect(to = '/')