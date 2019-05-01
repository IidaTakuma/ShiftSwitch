from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from main.models import Absence, Alternative
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class AbsenceChangeView(LoginRequiredMixin,View):
    model = Absence
    template_name = "main/absenceChange.html"

    def get(self, request, *args, **kwargs):
        error_msg = "postしてください"
        return render(request,"main/error.html",{'error_msg':error_msg})

    def post(self, request, *args, **kwargs):
        absence = Absence.objects.get(id = kwargs['pk'])
        absence.Alternative_user = request.user.id
        absence.is_settled = True
        absence.save()

        year = self.request.GET.get('y')
        month = self.request.GET.get('m')
        day = self.request.GET.get('d')
        week = self.request.GET.get('w')
        _date = str(year) + "-" + str(month) + "-" + str(day)

        Alternative.objects.filter(date=_date, Alternative_user=self.request.user.id).delete()

        messages.info(self.request, f'{absence.date}は{absence.Absence_user.mentor_name}さんの代わりに出勤します')

        return redirect('main:calender')