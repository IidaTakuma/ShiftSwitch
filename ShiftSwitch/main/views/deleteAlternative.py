from django.shortcuts import get_object_or_404,render, redirect
from django.views.generic import DeleteView
from main.models import Alternative
from users.models import User

class DeleteAlternativeView(DeleteView):
    model = Alternative
    template_name = 'main/deleteAlternative.html'
    success_url = "/"
