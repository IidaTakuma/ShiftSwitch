from django.shortcuts import render
from django.views.generic import CreateView
from main.models import Absence

class AbsenceCreateView(CreateView):
    model = Absence
    template_name = "main/absenceCreate.html"