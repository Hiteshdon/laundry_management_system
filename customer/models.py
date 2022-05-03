from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class UserDetail(models.Model):
    Id = models.SmallAutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Email_id = models.EmailField()
    Contact = models.CharField(max_length=10,default="0")
    Password = models.CharField(max_length=20)
    role= models.CharField(default="Customer", choices=(("customer","Customer"),("employee","Employee"),("manager","Manager"),("admins","Admin")), max_length=8)
    

    class Meta:
        verbose_name = "UserDetail"        
        verbose_name_plural = "UserDetails"

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("UserDetail", kwargs={"pk": self.pk})


class OrderDetail(models.Model):
    order_type_choices = [("Dry","Dry"),("Wash","Wash")]
    
    Id = models.SmallAutoField(primary_key=True)
    Cust_id = models.ForeignKey("customer.UserDetail",related_name="cust_id",  on_delete=models.SET_NULL, null=True)
    Emp_id = models.ForeignKey("customer.UserDetail",related_name="emp_id",  on_delete=models.SET_NULL, null=True)
    Order_cost = models.PositiveIntegerField()
    Order_type = models.CharField(max_length=4,choices=order_type_choices,default="Wash")
    Order_date = models.DateField()
    Pickup_date = models.DateTimeField(default=timezone.now)
    Coupon = models.CharField(max_length=6,default="")
    Machine = models.ForeignKey("employee.Machines",related_name="machine_id",null=True,blank=True,on_delete=models.SET_NULL)
    Time_Slot = models.CharField(max_length=6,null=True)
    
    class Meta:
        verbose_name = "OrderDetail"
        verbose_name_plural = "OrderDetails"

    def __str__(self):
        return str(self.Id)

    def get_absolute_url(self):
        return reverse("OrderDetail", kwargs={"pk": self.pk})
    

class DressesDetail(models.Model):
    id = models.SmallAutoField(primary_key=True)
    Dress_Name = models.CharField(unique=True,max_length=20)
    Cost = models.PositiveIntegerField()
    

    class Meta:
        verbose_name = "DressesDetail"
        verbose_name_plural = "DressesDetails"

    def __str__(self):
        return self.Dress_Name

    def get_absolute_url(self):
        return reverse("DressesDetail", kwargs={"pk": self.pk})

class Coupon(models.Model):
    Coupon= models.CharField(max_length=6,unique=True)
    Discount = models.PositiveIntegerField() 

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def __str__(self):
        return str(self.Discount)

    def get_absolute_url(self):
        return reverse("Coupon_detail", kwargs={"pk": self.pk})

class FeedBack(models.Model):
    Cust_id = models.ForeignKey("customer.UserDetail",related_name="Cust_id",  on_delete=models.SET_NULL, null=True)
    FeedbackId = models.SmallAutoField(primary_key=True)
    Feedback = models.TextField(max_length=150)
    Response = models.TextField(max_length=150)
    

    class Meta:
        verbose_name = "FeedBack"
        verbose_name_plural = "FeedBacks"

    def __str__(self):
        return (self.FeedbackId)

    def get_absolute_url(self):
        return reverse("FeedBack_detail", kwargs={"pk": self.pk})
