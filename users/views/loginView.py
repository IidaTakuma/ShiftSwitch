from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()

class OriginalLoginForm(LoginView):
    template_name = 'users/login.html'