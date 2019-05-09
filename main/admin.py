from django.contrib import admin
from .models import Profile, Absence, Alternative
# Register your models here.
admin.site.register(Profile)
admin.site.register(Absence)
admin.site.register(Alternative)