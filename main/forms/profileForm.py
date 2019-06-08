from django import forms
from users.models import User

class ProfileForm(forms.ModelForm):

    CHOICES = (
        ('BOTH','全日',),
        ('AM','AMのみ',),
        ('PM','PMのみ',),
        ('None','休み'),
    )

    shift_Sat = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=False, label="土曜固定")
    shift_Sun = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=False, label="日曜固定")

    class Meta:
        model = User
        fields = ("username", "shift_Sat", "shift_Sun", "is_board")

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'