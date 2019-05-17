from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, get_user_model
from users.forms import LoginForm

User = get_user_model()

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm