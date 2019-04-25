from django.urls import path
from . import views
from .views import *
from accounts import views
from django.contrib.auth import views as auth_views
from accounts.views import OriginalLoginForm

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', OriginalLoginForm.as_view(), name='login'),
]
