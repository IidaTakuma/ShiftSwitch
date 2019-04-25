from django import forms
from main.models import Absence
from users.models import User

class AbsenceCreateForm(forms.ModelForm):
    comment = forms.CharField(max_length=200,widget=forms.Textarea)

    CHOICES = (
        ('AM','AMのみ',),
        ('PM','PMのみ',),
        ('BOTH','全日',)
    )

    shift_zone = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False)

    class Meta:
        model = Absence
        fields = ("shift_zone", "comment",)