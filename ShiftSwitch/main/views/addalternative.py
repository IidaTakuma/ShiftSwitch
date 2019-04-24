from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from main.models import Absence

class AddAlternativeView(View):
    model = Absence
    template_name = "main/addalternative"

    def get(self, request, *args, **kwargs):
        error_msg = "postしてください"
        return render(request,"main/error.html",{'error_msg':error_msg})

    def post(self, request, *args, **kwargs):
        absence = Absence.objects.get(id = kwargs['pk'])
        absence.Alternative_user = request.user.id
        absence.save()
        return redirect('main:calender')
