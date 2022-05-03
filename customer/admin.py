from django.contrib import admin

from customer.models import Coupon, DressesDetail, FeedBack, OrderDetail, UserDetail

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(OrderDetail)
admin.site.register(DressesDetail)
admin.site.register(Coupon)
admin.site.register(FeedBack)