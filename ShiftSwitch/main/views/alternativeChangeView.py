from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from main.models import Alternative

class AlternativeChangeView(View):
    model = Alternative
    template_name = "main/alternativeChange.html"

    def get(self, request, *args, **kwargs):
        error_msg = "postしてください"
        return render(request,"main/error.html",{'error_msg':error_msg})

    def post(self, request, *args, **kwargs):
        alternative = Alternative.objects.get(id = kwargs['pk'])
        alternative.Absence_user = request.user.id
        alternative.save()
        return redirect('main:calender')
