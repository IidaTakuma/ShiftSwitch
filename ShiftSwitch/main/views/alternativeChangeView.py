from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from main.models import Alternative
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


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
        messages.info(self.request, f'{alternative.date}は{alternative.Alternative_user.mentor_name}さんに代わってもらいました')

        return redirect('main:calender')
