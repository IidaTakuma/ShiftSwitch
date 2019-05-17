from django.urls import path
from . import views
from .views import *
from users import views
from django.contrib.auth import views as auth_views
from users.views import CustomLoginView

app_name='users'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('regist/', UsersRegistView.as_view(), name='regist'),
    path('regist_done/', UsersRegistDone.as_view(), name='regist_done'),
    path('regist_complete/<token>/', UsersRegistComplete.as_view(), name='regist_complete'),

    path('password_change/',PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),

    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
]
