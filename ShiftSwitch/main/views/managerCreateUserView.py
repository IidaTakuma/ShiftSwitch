from django.views.generic import CreateView
from users.models import User
from django.shortcuts import redirect
from main.forms import CreateUserForm

class CreateUserView(CreateView):
    model = User
    template_name = "main/managerCreateUser.html"
    form_class = CreateUserForm

    def post(self, request, *args, **kwargs):
        _username = request.POST['username']
        _mentor_name = request.POST['username']
        _password = request.POST['password']
        
        user = User()
        user.username = _username
        user.mentor_name = _mentor_name
        user.set_password(_password)
        user.save()
        print(_username + "を作成しました")
        return redirect(to = '/')