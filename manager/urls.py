
from django.urls import include, path
from .views import *

obj = Other()
app_name="manager"
urlpatterns = [
    path("",obj.homepage,name='Homepage'),
    path("employee/",include("employee.urls"),name='Employee-Dashboard'),
    
    
    
]
