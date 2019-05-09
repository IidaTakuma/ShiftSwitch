from django import forms
from main.models import Absence,Alternative
from users.models import User

class AbsenceCreateForm(forms.ModelForm):
    comment = forms.CharField(max_length=200,widget=forms.Textarea, label='コメント')

    CHOICES = (
        ('BOTH','全日',),
        ('AM','AMのみ',),
        ('PM','PMのみ',),
    )

    shift_zone = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=False,label='時間帯')

    class Meta:
        model = Absence
        fields = ("shift_zone", "comment",)

class AlternativeCreateForm(forms.ModelForm):
    comment = forms.CharField(max_length=200,widget=forms.Textarea,label="コメント")

    CHOICES = (
        ('BOTH','全日',),
        ('AM','AMのみ',),
        ('PM','PMのみ',),
    )

    shift_zone = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=False)

    class Meta:
        model = Alternative
        fields = ("shift_zone", "comment",)