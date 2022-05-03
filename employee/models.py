from django.db import models
from django.urls import reverse

# Create your models here.


class OrderDresses(models.Model):
    Order_id = models.ForeignKey("customer.OrderDetail",related_name="order_id",null=True,on_delete=models.SET_NULL)
    Dress_id = models.ForeignKey("customer.DressesDetail",related_name="dress_id",null=True,on_delete=models.SET_NULL)
    Quantity = models.PositiveSmallIntegerField(default=0)
    cost = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = "OrderDresses"
        verbose_name_plural = "OrderDresses"

    def __str__(self):
        return self.Order_id

    def get_absolute_url(self):
        return reverse("OrderDresses_detail", kwargs={"pk": self.pk})


class InventoryDetail(models.Model):
    id = models.SmallAutoField(primary_key=True)
    Supply_Name = models.CharField(max_length=20,unique=True)
    Quantity = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = "InventoryDetail"
        verbose_name_plural = "InventoryDetails"

    def __str__(self):
        return self.Supply_Name

    def get_absolute_url(self):
        return reverse("InventoryDetail", kwargs={"pk": self.pk})

class Machines(models.Model):
    id = models.SmallAutoField(primary_key=True)
    Machine_name = models.CharField(max_length=10,unique=True)
    Type = models.CharField(choices=(("dryer","Dryer"),("washer","Washer")),max_length=6)
    Status = models.CharField(choices = (("working","Working"),("damaged","Damaged")),default ="working",max_length=7)
    
    class Meta:
        verbose_name = ("Machine")
        verbose_name_plural = ("Machines")

    def __str__(self):
        return self.Machine_name

    def get_absolute_url(self):
        return reverse("Machines_detail", kwargs={"pk": self.pk})
