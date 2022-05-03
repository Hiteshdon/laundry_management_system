from django.urls import path

from .views import Other


obj = Other()
app_name="employee"
urlpatterns = [
    path("", obj.homepage,name='Homepage'),
    path("machine_status/", obj.status,name="Machine Status"),
    path("customer/", obj.inventory,name="Inventory"),
    path("customer/<int:item>", obj.inventory1,name="Add Supply"),
    
]
