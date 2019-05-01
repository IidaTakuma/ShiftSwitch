from django.shortcuts import render, redirect
from django.views.generic import CreateView
from main.models import Alternative
from main.forms.createForm import AlternativeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class AlternativeCreateView(LoginRequiredMixin,CreateView):
    model = Alternative
    template_name = "main/alternativeCreate.html"
    form_class = AlternativeCreateForm

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
        
        alternative = Alternative()
        alternative.shift_zone = _shift_zone
        alternative.comment = _comment
        alternative.Alternative_user = request.user
        alternative.date = self.get_date()
        alternative.save()
        messages.info(self.request, f'{alternative.date}の出勤申請をしました。')

        return redirect(to = '/')