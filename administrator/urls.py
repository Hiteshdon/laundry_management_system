from django.urls import path, include

from .views import Other

obj = Other()
app_name = 'admins'
urlpatterns = [
    path("",obj.homepage,name='Homepage'),
    path("manager/",include('manager.urls'),name="Manager-Dashboard"),
    path("employee/",include('employee.urls'),name="Employee-Dashboard"),
    path("customer_details/",obj.customers,name="Customers-Details"),
    path("customer_details/<int:item>",obj.customer,name="Customer-Details"),
    path("employee_details/",obj.employees,name="Employees-Details"),
    path("employee_details/<int:item>",obj.employee,name="Employee-Details"),
    
]
