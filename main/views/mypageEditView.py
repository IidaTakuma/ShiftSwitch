from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from users.models import User
from main.forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .methods import *


class MyPageEditView(LoginRequiredMixin,UpdateView):
    model =  User
    template_name = "main/mypageEdit.html"
    form_class = ProfileForm
    success_url = "/"

    def form_valid(self, form):
        messages.info(self.request, f'プロフィールを編集を保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, f'プロフィールの保存に失敗しました')
        return super().form_invalid(form)