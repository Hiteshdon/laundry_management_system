from genericpath import exists
from operator import methodcaller
from django.core.mail import EmailMessage
from multiprocessing import context
import pdb
from django.http import QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse
from customer.context_processors import message_processor
from customer.forms import  LoginForm, OrderDetailForm, SignUpForm

from employee.models import OrderDresses
from customer.models import Coupon, DressesDetail, FeedBack, OrderDetail, UserDetail
from laundry_system.settings import EMAIL_HOST_USER
from django.template.context_processors import csrf

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class Home:
    context = {"value": True}
    data = {}
    dress_list = []

    def homepage_other(self, request):
        self.context["value"] = True
        dresses = DressesDetail.objects.all()
        self.context.update({})
        new = {'dresses': dresses}
        new.update(self.context)
        
        # new=csrf(new)
        if request.method == "POST":  # if form sends POST request then, create customer
            message_processor(request)
            # pdb.set_trace()
            print("Post data:", request.POST)
            # if POST data has 6 fields(i.e name, email, password, contact, csrf_token, submit_button) then create customer with validations, else UserDetail autheticate
            if len(request.POST) == 6:  
                form = SignUpForm(request.POST)
                form.save()
            elif len(request.POST) == 4:
                form = LoginForm(request.POST)
                # x = auth.authenticate(username=UserDetail.objects.get(username=email1).username,password=password1)
                if form.is_valid():
                    x = UserDetail.objects.get(Email_id=form.cleaned_data.get("Email_id"), Password=form.cleaned_data.get("Password"))
                    if x is not None:
                        path = x.role
                        self.context["id"] = x.Id
                return redirect("/"+path+"/")
            elif len(request.POST) == 2:
                email1 = request.POST["email1"]
                x = UserDetail.objects.filter(Email_id=email1)
                if len(x) == 1:
                    mail = EmailMessage(
                        "Forgot Password", "Your Password is "+x.first().Password, EMAIL_HOST_USER, [email1])
                    mail.send()
                return redirect("/")
            return redirect("/login")
        else:
            return render(request, "customer\home.html", new)
                    
                    
                    
                
                
            

    def homepage(self, request):
        self.context["value"] = False
        # print(self.context)
        dresses = DressesDetail.objects.all()
        self.context["order_form"] = OrderDetailForm()
        new = {"dresses": dresses} 
        if request.method == 'POST':
            # Add dresses in the list
            if "submit" in request.POST:
                dress = DressesDetail.objects.filter(id=request.POST["Dresses_List"]).first()
                total = 0
                if int(request.POST["quantity"])>0:
                    if len(self.dress_list) > 0:
                        for i, item in enumerate(self.dress_list):
                            if item['Dress_Name'] == dress.Dress_Name:
                                self.dress_list[i] = {"Dress_Name": dress.Dress_Name,"quantity": request.POST["quantity"], "cost": dress.Cost*int(request.POST["quantity"])}
                                break
                        else:
                            self.dress_list += [{"Dress_Name": dress.Dress_Name,
                                         "quantity":request.POST["quantity"], "cost":dress.Cost*int(request.POST["quantity"])}]
                        total = sum([i["cost"] for i in self.dress_list])
                    else:
                        self.dress_list += [{"Dress_Name": dress.Dress_Name,
                                     "quantity":request.POST["quantity"], "cost":dress.Cost*int(request.POST["quantity"])}]
                        total = dress.Cost*int(request.POST["quantity"])
                elif int(request.POST["quantity"])<=0:
                    for i, item in enumerate(self.dress_list):
                        if item['Dress_Name'] == dress.Dress_Name:
                            self.dress_list.pop(i)
                new["date"] = request.POST["Order_date"]
                
                if 'Time_Slot' in request.POST:
                    if request.POST['Time_Slot'] == "0":
                        new["slot"] = "Today"
                    else:
                        new["slot"] = request.POST["Time_Slot"]+":00"
                if 'Coupon' in request.POST and len(request.POST['Coupon']) > 0:
                    coupon = Coupon.objects.get(Coupon=request.POST['Coupon']).Discount
                    if (coupon <= total*0.05):
                        new["hasCoupon"] = True
                        new["Coupon"] = Coupon.objects.get(Coupon=request.POST['Coupon']).Coupon
                        new["coupon_cost"] = coupon
                        total -= coupon
                    elif (coupon <= total*0.10):
                        new["hasCoupon"] = True
                        new["Coupon"] = Coupon.objects.get(Coupon=request.POST['Coupon']).Coupon
                        new["coupon_cost"] = coupon
                        total -= coupon
                    elif (coupon <= total*0.15):
                        new["hasCoupon"] = True
                        new["Coupon"] = Coupon.objects.get(Coupon=request.POST['Coupon']).Coupon
                        new["coupon_cost"] = coupon
                        total -= coupon
                    elif (coupon <= total*0.25):
                        new["hasCoupon"] = True
                        new["Coupon"] = Coupon.objects.get(Coupon=request.POST['Coupon']).Coupon
                        new["coupon_cost"] = coupon
                        total -= coupon
                    elif (coupon <= total*0.5):
                        new["hasCoupon"] = True
                        new["Coupon"] = Coupon.objects.get(
                            Coupon=request.POST['Coupon']).Coupon
                        new["coupon_cost"] = coupon
                        total -= coupon
                new["pickup"] = request.POST["Pickup_date_0"] +" "+request.POST["Pickup_date_1"]
                new["dress_list"] = self.dress_list
                new["type"] = request.POST["Order_type"]
                new['total'] = total
                new["show"] = len(self.dress_list) > 0
                self.data = dict(new)
            print("ID:","id" in self.context)
            if "Book" in request.POST and "id" in self.context:
                print(self.data)
                data = ["total", "type", "dress_list","pickup", "Coupon", "date", "slot"]
                length = len(list(filter(lambda each_item: each_item in self.data, data)))
                print(length  == len(data))
                if length  == len(data) or length == len(data)-1:
                    print("\n\nOrder is created")
                    if length == len(data)-1: self.data["Coupon"]=""
                    length1  = len(list(filter(lambda each_item: len(str((self.data[each_item]))) > 0, data)))
                    print(length1 == len(data) or length1 == len(data)-1)
                    if  length1 == len(data) or length1 == len(data)-1:
                        x = OrderDetail.objects.create(
                            Cust_id=UserDetail.objects.get(Id=self.context["id"]), Order_cost=self.data["total"],
                            Order_type=self.data["type"],
                            Order_date=self.data["date"],
                            Pickup_date=self.data["pickup"],
                            Coupon=self.data["Coupon"],
                            Time_Slot=self.data["slot"])
                        x.save()
                        print("\n\nOrder is Successfull")
                        for  i in self.data["dress_list"]:
                            id = DressesDetail.objects.get(Dress_Name=i["Dress_Name"])
                            OrderDresses.objects.create(Order_id=x,Dress_id=id,Quantity=i["quantity"],cost=i["cost"]).save()
                            print("dresses Saved")
                        mail = EmailMessage("Order Created","Dear Customer, \n\n Your Order (ID: "+x.Id+") is Created successfully.",EMAIL_HOST_USER,[x.Cust_id.Email_id]) 
                        mail.send()
                self.dress_list.clear()
        new.update(self.context)
        if request.method == "POST": new["order_form"] = OrderDetailForm(request.POST)
        # new = csrf(new)
        
        return render(request, 'customer\order.html', new)


class Other(Home):

    def profile(self, request):
        self.context["value"] = False
        if "id" in self.context:
            user = UserDetail.objects.get(Id=self.context["id"])
            new = {"Name": user.Name, "Password_hidden": user.Password,
                   "Email_id": user.Email_id, "Contact": user.Contact}
            if request.method == "POST":

                if 'edit' in request.POST:
                    new["edit"] = True
                elif 'save' in request.POST:
                    new["Name"] = request.POST["name"]
                    new["Email_id"] = request.POST["email"]
                    new["Contact"] = request.POST['contact']
                    new["Password_hidden"] = request.POST["password"]
                    x = UserDetail.objects.filter(Id=self.context["id"]).update(
                     Email_id=new["Email_id"], Name=new["Name"], Password=new["Password_hidden"], Contact=new["Contact"])
                    print("Update:", x)
                    new['edit'] = False
                elif 'delete' in request.POST:
                    x = UserDetail.objects.filter(Id=self.context["id"]).delete()
                    print("Delete:", x)
                    return redirect("/")
            new.update(self.context)
            return render(request, "customer\profile.html", new)
        else:
            return render(request, "customer\home.html", self.context)
            # new = csrf(new)
            

    def ordersHistory(self, request):
        dresses = DressesDetail.objects.all()
        if 'id' in self.context:
            new = {"dresses": dresses,"mydata":13} 
            new["order_form1"]=OrderDetailForm()
            orders = OrderDetail.objects.filter(Cust_id=self.context["id"])
            new["hasOrders"] = len(orders) > 0
            if new["hasOrders"]:
                new["orders"] = orders
            if request.method == "GET" and is_ajax(request=request):
                x=OrderDetail.objects.get(Id=request.GET["id"])
                data ={"Order_date":x.Order_date,"Order_type":x.Order_type,"Time_Slot":x.Time_Slot,"Pickup_date":x.Pickup_date}
                new["order_form1"]=OrderDetailForm(QueryDict.dict(data))
                new["order_form1"].helper.form_id="edit_form"
                
            if request.method == "POST":
                if "sendFeedback" in request.POST:
                    toEmail = UserDetail.objects.get(Id=self.context["id"])
                    mail = EmailMessage("Customer Feedback",request.POST["feedback"],EMAIL_HOST_USER,[toEmail.Email_id]) 
                    mail.send() 
                    db = FeedBack(Cust_id=toEmail,Feedback=request.POST["feedback"])
                    db.save()
            new.update(self.context)
            return render(request, "customer/order_history.html", new)
        else:
            return render(request, "customer\home.html", self.context)
        
        
        
    
