from django.shortcuts import get_object_or_404,render, redirect
from django.views.generic import DeleteView
from main.models import Alternative
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class DeleteAlternativeView(LoginRequiredMixin, DeleteView):
    model = Alternative
    template_name = 'main/alternativeDelete.html'
    success_url = "/"
