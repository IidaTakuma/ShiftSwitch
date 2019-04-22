from django.db import models
from users.models import User

class Absence(models.Model):
    Absence_user = models.ForeignKey(User, verbose_name="休む人", on_delete=models.CASCADE)
    Alternative_user = models.IntegerField(verbose_name="代わりに入る人", blank=True)
    date = models.DateField()
    shift_zone = models.CharField(max_length=15)
    is_settled = models.BooleanField(default=False)