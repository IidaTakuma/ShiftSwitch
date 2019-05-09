from django import forms
from users.models import User

class CreateUserForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("email",)