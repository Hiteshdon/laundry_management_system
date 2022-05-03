import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from customer.models import OrderDetail

from employee.models import InventoryDetail, Machines

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
class Home:
    
    def __init__(self,context = {"page":'employee\main.html',}):
        self.context=context
    
    def homepage(self,request):
        return render(request,'employee\dashboard.html',self.context)
    
    
class Other(Home):
    
    def __init__(self, context={ "page": 'employee\main.html' }):
        super().__init__(context)
    
    def inventory(self,request):
        items = InventoryDetail.objects.all()
        print("Something Changed")
        new = {"supply_items":items}
        new.update(self.context)
        return render(request,"employee\inventory.html",new)
    
    def inventory1(self,request,item):
        items = InventoryDetail.objects.all()
        item = InventoryDetail.objects.filter(pk=int(item)).first()
        new = {"supply_items":items,"supply_item":item}
        new.update(self.context)
        return render(request,"employee\inventory.html",new)

    def status(self,request):
        self.context= {"page":'employee\main.html'} 
        if is_ajax(request=request) and request.method == "GET":
            machines = serializers.serialize('json', Machines.objects.all())
            orders= []
            if "Id" in request.GET:orders = [{"id":str(i.Id),"machine":str(i.Machine)}  for i in OrderDetail.objects.filter(Time_Slot=request.GET["Id"]+":00")]
            resp ={"machines":machines,"orders":json.dumps(orders)}
            return HttpResponse(json.dumps(resp),content_type="application/json")
        return render(request,"employee\status.html",self.context)