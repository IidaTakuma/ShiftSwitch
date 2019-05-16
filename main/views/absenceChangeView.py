from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from main.models import Absence, Alternative
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .methods import * #汎用なメソッド


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

        _date = get_date(self)

        Alternative.objects.filter(date=_date, Alternative_user=self.request.user.id).delete()

        messages.info(self.request, f'{absence.date}は{absence.Absence_user.username}さんの代わりに出勤します')

        return redirect('main:calender')