from django.shortcuts import get_object_or_404,render, redirect
from django.views.generic import DeleteView
from main.models import Absence
from users.models import User
from django.contrib.auth.decorators import login_required

class DeleteAbsenceView(DeleteView):
    model = Absence
    template_name = 'main/deleteAbsence.html'
    success_url = "/"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     _user = self.request.user
    #     context['absence_object'] = Absence.objects.get(Absence_user = _user)
    #     return context
    
