from django.contrib import admin

from customer.models import OrderDetail
from employee.models import InventoryDetail, Machines, OrderDresses

# Register your models here.
admin.site.register(OrderDresses)
admin.site.register(InventoryDetail)
admin.site.register(Machines)