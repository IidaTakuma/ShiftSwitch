from django.views.generic import CreateView
from users.models import User
from django.shortcuts import redirect
from main.forms import CreateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateUserView(LoginRequiredMixin, CreateView):
    model = User
    template_name = "main/managerCreateUser.html"
    form_class = CreateUserForm

    def post(self, request, *args, **kwargs):
        _username = "ユーザ名は設定されていません"
        _password = "admin012"
        
        user = User()
        user.username = _username
        user.set_password(_password)
        user.save()
        print(_username + "を作成しました")
        return redirect(to = '/')