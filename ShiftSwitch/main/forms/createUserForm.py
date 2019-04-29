from django import forms
from users.models import User

class CreateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    mentor_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ("username", "mentor_name","password")