from django.views.generic import FormView
from django import forms
from users.models import User


class RegistForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")
        
class RegistView(FormView):
    template_name = 'users/regist.html'
    form_class = RegistForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)