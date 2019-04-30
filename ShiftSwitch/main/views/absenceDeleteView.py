from django.shortcuts import get_object_or_404,render, redirect
from django.views.generic import DeleteView
from main.models import Absence
from users.models import User

class DeleteAbsenceView(DeleteView):
    model = Absence
    template_name = 'main/absenceDelete.html'
    success_url = "/"
