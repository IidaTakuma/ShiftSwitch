from django.db import models
from users.models import User

class Absence(models.Model):
    Absence_user = models.ForeignKey(User, verbose_name="休む人", on_delete=models.CASCADE)
    Alternative_user = models.IntegerField(verbose_name="代わりに入る人", default=-1)
    date = models.DateField()
    shift_zone = models.CharField(max_length=15)
    comment = models.TextField(max_length=200, default="なし")
    is_settled = models.BooleanField(default=False)


    def get_user_from_id(self):
        user = User.objects.get(id=self.Alternative_user)
        return user