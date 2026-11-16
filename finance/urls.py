from django.urls import path, include
from .views import *

urlpatterns = [
    path("", registration, name="registration"),
    path("login/", login_user, name="login"),
    path('home' ,home, name='home'),
    path('create_wallet/', create_wallet, name='create_wallet'),
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', withdraw, name='withdraw'),
    path('history/', history, name='history'),
    path('add_history', create_history, name='add_history')
]
