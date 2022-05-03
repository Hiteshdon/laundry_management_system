from datetime import  datetime, timedelta
from django.shortcuts import render

from customer.models import OrderDetail, UserDetail
from employee.models import Machines

# Create your views here.

    
class Home:
    def __init__(self,context= {"page":"administrator\main.html"}):
        self.context= context 
    
    def homepage(self, request):
        weekly_data = []
        weeks =[]
        today_amount = 0
        for days in range(7):
            dday = datetime.today() - timedelta(days=-(days))
            order_list = OrderDetail.objects.filter(Order_date = dday)
            total = 0
            print(order_list.count())
            for i in order_list:
                
                if i.Machine in Machines.objects.all(): 
                    if dday == datetime.today() : today_amount += int(i.Order_cost)
                    total += int(i.Order_cost)
                    
            weekly_data.append(total)
            weeks.append(dday.weekday())
        if request.method == "POST":
            name1 = request.POST['name']
            email1 = request.POST['email']
            password1 = request.POST['password']
            contact = request.POST['contact1']
            role = request.POST['role']
            x = UserDetail.objects.create(role=role,Email_id=email1,Name=name1,Password=password1,Contact=contact)
            x.save()
        pending_orders = OrderDetail.objects.filter(Order_date=datetime.today(),Machine=None).count()
        
        today_orders = OrderDetail.objects.filter(Order_date=datetime.today()).count()
        total_Customers = UserDetail.objects.filter(role="customer").count()
        total_employees = UserDetail.objects.filter(role="employee").count() +UserDetail.objects.filter(role="manager").count()
        total_orders = 0
        for order in OrderDetail.objects.all():
            if  datetime.strptime(str(order.Order_date),"%Y-%m-%d") <= datetime.today():
                today_orders +=1
        new = {
            "total_orders":total_orders,
            "total_customers":total_Customers,
            "total_employees":total_employees,
            "today_amount":today_amount,
            "pending_orders":pending_orders,
            "today_orders":today_orders,
            "weekly_data":weekly_data[::-1],
            "weeks":weeks[::-1]}
        new.update(self.context)
        return render(request,'administrator\dashboard.html',new)

class Other(Home):
    
    def __init__(self, context={ "page": "administrator\main.html" }):
        super().__init__(context)
    
    def customers(self,request):
        user = UserDetail.objects.filter(role="customer").all()
        first_user = UserDetail.objects.filter(role='customer').first()
        new = {"users":user,"first_user":first_user}
        if request.method == "POST" and len(request.POST) == 2:
            if "id" in request.POST:
                id = request.POST["id"]
                user = UserDetail.objects.filter(Id=id).delete()
                print(user)
        if request.method =="GET" and len(request.GET) == 1:
            new["users"] = UserDetail.objects.filter(Name__icontains=request.GET['search'],role='customer')
            new["first_user"] = new["users"].first()
        new.update(self.context)
        return render(request,'administrator\customer.html',new)
    
    def customer(self,request,item):
        user = UserDetail.objects.filter(role="customer").all()
        first_user = UserDetail.objects.filter(role='customer',Id=item).first()
        new = {"users":user,"first_user":first_user}
        if request.method =="GET" and len(request.GET) == 1:
            new["users"] = UserDetail.objects.filter(Name__icontains=request.GET['search'],role='customer')
            new["first_user"] = new["users"].first()
        new.update(self.context)
        return render(request,'administrator\customer.html',new)

    def employees(self,request):
        user = list(UserDetail.objects.filter(role="employee").all()) + list(UserDetail.objects.filter(role="manager").all())
        first_user = UserDetail.objects.filter(role='employee').first()
        new = {"users":user,"first_user":first_user}
        if request.method == "POST" and len(request.POST) == 2:
            if "role" in request.POST:
                role = request.POST["role"].split()[0]
                id = request.POST["role"].split()[1]
                user = UserDetail.objects.filter(Id=id).update(role=role)
                print(user)
            elif "id" in request.POST:
                id = request.POST["id"]
                user = UserDetail.objects.filter(Id=id).delete()
                print(user)
        elif request.method == "GET" and len(request.GET) == 0:
            print("Something")
        elif request.method =="GET" and len(request.GET) == 1:
            new["users"] = UserDetail.objects.filter(Name__icontains=request.GET['search'],role='employee')
            new["first_user"] = new["users"].first()
        new.update(self.context)
        return render(request,'administrator\employee.html',new)
    
    def employee(self,request, item):
        user = list(UserDetail.objects.filter(role="employee").all()) + list(UserDetail.objects.filter(role="manager").all())
        first_user = UserDetail.objects.filter(role='employee',Id=item).first()
        new = {"users":user,"first_user":first_user}
        if request.method == "GET" and len(request.GET) == 0:
            print("Something")
        if request.method =="GET" and len(request.GET) == 1:
            new["users"] = UserDetail.objects.filter(Name__icontains=request.GET['search'],role='employee')
            new["first_user"] = new["users"].first()
        new.update(self.context)
        return render(request,'administrator\employee.html',new)