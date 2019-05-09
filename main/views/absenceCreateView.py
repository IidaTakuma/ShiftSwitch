from django.shortcuts import render, redirect
from django.views.generic import CreateView
from main.models import Absence
from main.forms.createForm import AbsenceCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .methods import *


class AbsenceCreateView(LoginRequiredMixin,CreateView):
    model = Absence
    template_name = "main/absenceCreate.html"
    form_class = AbsenceCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_dateData_to_context(self, context)
        return context

    def post(self, request, *args, **kwargs):

        _shift_zone = request.POST['shift_zone']
        _comment = request.POST['comment']
        
        absence = Absence()
        absence.shift_zone = _shift_zone
        absence.comment = _comment
        absence.Absence_user = request.user
        absence.date = get_date(self)
        absence.save()
        messages.info(self.request, f'{absence.date}の欠席申請をしました。')

        return redirect(to = '/')