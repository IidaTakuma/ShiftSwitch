from django.shortcuts import render, redirect
from django.views.generic import CreateView
from main.models import Alternative
from main.forms.createForm import AlternativeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .methods import * #汎用なメソッド


class AlternativeCreateView(LoginRequiredMixin,CreateView):
    model = Alternative
    template_name = "main/alternativeCreate.html"
    form_class = AlternativeCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_dateData_to_context(self, context)

        return context

    def post(self, request, *args, **kwargs):

        _shift_zone = request.POST['shift_zone']
        _comment = request.POST['comment']
        
        alternative = Alternative()
        alternative.shift_zone = _shift_zone
        alternative.comment = _comment
        alternative.Alternative_user = request.user
        alternative.date = get_date(self)
        alternative.save()
        messages.info(self.request, f'{alternative.date}の出勤申請をしました。')

        return redirect(to = '/')