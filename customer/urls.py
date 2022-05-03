import profile
from django.urls import path

from .views import *

obj = Other()
app_name = 'CUSTOMER'
urlpatterns = [
    path("",obj.homepage,name='Homepage'),
    path("profile/",obj.profile,name='ProfilePage'),
    path("orders/",obj.ordersHistory,name="Order History"),
]
