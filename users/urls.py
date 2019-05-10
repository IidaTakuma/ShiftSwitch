from django.urls import path
from . import views
from .views import *
from users import views
from django.contrib.auth import views as auth_views
from users.views import OriginalLoginForm

app_name='users'

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', OriginalLoginForm.as_view(), name='login'),
    path('create_complete/<slug:uidb64>/',CreateCompleteView.as_view(), name='create_complete'),
    # path('regist/', views.regist, name='regist'),
    # path('regist_save/', views.regist_save, name='regist_save'),
]
