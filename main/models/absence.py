from django.db import models
from users.models import User

class Absence(models.Model):
    Absence_user = models.ForeignKey(User, verbose_name="休む人", on_delete=models.CASCADE)
    Alternative_user = models.IntegerField(verbose_name="代わりに入る人", default=-1)
    date = models.DateField()
    shift_zone = models.CharField(max_length=15)
    comment = models.TextField(max_length=200, default="なし")
    is_settled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Absence_user.username) + " " + str(self.date)

    def get_mentor_name_from_id(self):
        user = User.objects.get(id=self.Alternative_user)
        _mentor_name = user.username
        return _mentor_name

    def shift_zone_judge_AM(self):
        _shift_zone = self.shift_zone
        if _shift_zone == "AM" or _shift_zone == "BOTH":
            return True
        
        return False

    def shift_zone_judge_PM(self):
        _shift_zone = self.shift_zone
        if _shift_zone == "PM" or _shift_zone == "BOTH":
            return True
        
        return False