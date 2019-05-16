from django import template
from main.models import Absence, Alternative, Profile

register = template.Library()

@register.filter(name='count_deficiency')

def count_deficiency(day):
    year = day[0]
    month = day[1]
    day = day[2]

    _date = str(year)+"-"+str(month)+"-"+str(day)

    is_absence = Absence.objects.filter(date=_date).filter(is_settled=False).count()
    is_alternative = Alternative.objects.filter(date=_date).filter(is_settled=False).count()
    deficiency = is_alternative - is_absence

    return deficiency

