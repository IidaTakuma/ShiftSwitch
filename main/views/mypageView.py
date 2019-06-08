from django.views.generic import TemplateView
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class MyPageView(LoginRequiredMixin,TemplateView):
    models = User
    template_name = "main/mypage.html"