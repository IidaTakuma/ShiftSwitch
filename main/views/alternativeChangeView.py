from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from main.models import Alternative, Absence
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .methods import * #汎用なメソッド


class AlternativeChangeView(LoginRequiredMixin,View):
    model = Alternative
    template_name = "main/alternativeChange.html"

    def get(self, request, *args, **kwargs):
        error_msg = "postしてください"
        return render(request,"main/error.html",{'error_msg':error_msg})

    def post(self, request, *args, **kwargs):
        alternative = Alternative.objects.get(id = kwargs['pk'])
        alternative.Absence_user = request.user.id
        alternative.is_settled = True
        alternative.save()

        _date = get_date(self)

        Absence.objects.filter(date=_date, Absence_user = self.request.user.id).delete()

        messages.info(self.request, f'{alternative.date}は{alternative.Alternative_user.username}さんに代わってもらいました')

        return redirect('main:calender')
