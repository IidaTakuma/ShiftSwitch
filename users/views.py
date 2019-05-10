# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from .models import User, Activate
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

User = get_user_model()

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email',)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


class OriginalLoginForm(LoginView):
    template_name = 'users/login.html'

# class RegisterForm(UserCreationForm):
#     user
#     email = forms.EmailField(required=True)

class CreateCompleteView(TemplateView):
    template_name = 'users/create_complete.html'

    def get(self, request, **kwargs):
        uidb64 = kwargs.get("uidb64")
 
        try:
            #keyをデコード
            key = force_text(urlsafe_base64_decode(uidb64))
          
            # keyを使ってactivateモデルを取得
            activate = get_object_or_404(Activate, key=key)
 
            # activateモデルに紐付いたユーザオブジェクトを取得
            user = activate.user
 
            #有効期限取得
            expiration_date = activate.expiration_date
            t_now = datetime.datetime.now(datetime.timezone.utc)
 
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
 
        if user and not user.is_active and t_now <= expiration_date:
            context = super(CreateCompleteView, self).get_context_data(**kwargs)
 
            # ユーザをアクティブに変更
            user.is_active = True
            user.save()
 
            # 本登録後、ログイン処理
            user.backend = 'users.backends.EmailModelBackend'
            login(request, user)
 
            # ページに表示するメッセージ
            response_message = "本登録が完了しました。"
            context["message"] = response_message
 
            # 仮登録用トークン削除
            Activate.objects.filter(key=key).delete()
 
            return render(self.request, self.template_name, context)
        else:
 
            # 仮登録用トークン削除
            Activate.objects.filter(key=key).delete()
 
            if user :
                # 仮登録ユーザ削除
                User.objects.filter(id=user.id).delete()

            return render(request, 'users/create_failed.html')
