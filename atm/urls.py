from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('check-balance/', views.check_balance, name='check_balance'),
    path('deposit-money/', views.deposit_money, name='deposit_money'),
    path('withdraw-money/', views.withdraw_money, name='withdraw_money'),
    path('change-pin/', views.change_pin, name='change_pin'),
    path('logout/', views.logout, name='logout'),
]
