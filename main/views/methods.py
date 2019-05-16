
def get_date(object):

    year = object.request.GET.get('y')
    month = object.request.GET.get('m')
    day = object.request.GET.get('d')
    week = object.request.GET.get('w')
    date = str(year) + "-" + str(month) + "-" + str(day)

    return date

def set_dateData_to_context(object, context):

    year = object.request.GET.get('y')
    month = object.request.GET.get('m')
    day = object.request.GET.get('d')
    week = object.request.GET.get('w')

    context["year"] = year
    context["month"] = month
    context["day"] = day
    context["week"] = week

    return