from django.views.generic import TemplateView
from main.models import Profile
from users.models import User

class MyPageView(TemplateView):
    models = User
    template_name = "main/mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _user = self.request.user
        context['profile'] = Profile.objects.get(user = _user)
        return context