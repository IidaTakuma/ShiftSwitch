from django.db import models
from users.models import User

class Alternative(models.Model):
    Absence_user = models.IntegerField(verbose_name="休む人", blank=True)
    Alternative_user = models.ForeignKey(User, verbose_name="代わりに入る人", on_delete=models.CASCADE)
    date = models.DateField()
    shift_zone = models.CharField(max_length=15)
    is_settled = models.BooleanField(default=False)