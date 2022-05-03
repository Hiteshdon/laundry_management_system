
from datetime import date, datetime
from xml.dom.minidom import AttributeList
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from customer.models import DressesDetail, OrderDetail, UserDetail
from customer.validators import validate_domainonly_email

class SplitDateTimeWidget(forms.SplitDateTimeWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def subwidgets(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        return context['widget']['subwidgets']
    
# creating a form 
class SignUpForm(forms.ModelForm):
    Name = forms.CharField(required=True, min_length=3,label="Name")
    Email_id = forms.EmailField(required=True,validators=[validate_domainonly_email])
    Contact = forms.CharField(max_length=10,required=True)
    Password = forms.CharField(required=True,widget=forms.PasswordInput(),max_length=13,min_length=6)
    
    class Meta:
        model = UserDetail
        fields = ["Name" ,"Email_id","Contact" ,"Password"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'SignUpForm'
        self.helper.form_class = 'form d-grid'
        self.helper.form_method = 'post'
        self.helper.form_action = "/login/"
        self.helper.layout = Layout("Name" ,"Email_id","Contact" ,"Password",Submit('submit', 'Sign Up',css_class="mt-3"))
    
    def clean_Email_id(self):
        data = self.cleaned_data.get("Email_id")
        if self.Meta.model.objects.filter(Email_id=data).exists():
            raise forms.ValidationError("Email id already exists")
        return data
    
    def clean_Contact(self):
        data = self.cleaned_data.get("Contact")
        if self.Meta.model.objects.filter(Contact=data).exists():
            raise forms.ValidationError("Contact number is already exists")
        return data

class LoginForm(forms.ModelForm):
    Email_id = forms.EmailField(required=True)
    Password = forms.CharField(required=True,widget=forms.PasswordInput(),min_length=6)
    
    class Meta:
        model = UserDetail
        fields = ["Email_id","Password"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'LoginForm'
        self.helper.form_class = 'form'
        self.helper.form_method = 'post'
        self.helper.form_action = "/login/"
        self.helper.layout = Layout("Email_id","Password",HTML("""<a href='/login' data-bs-toggle='modal' data-bs-target='#forgot_password'>Forgot Password</a><br/>"""),Submit('submit', 'Sign Up',css_class="mt-2"))
    
    def clean_Email_id(self):
        data = self.cleaned_data.get("Email_id")
        if not self.Meta.model.objects.filter(Email_id=data).exists():
            raise forms.ValidationError("Email id doesn't exists")
        return data


class OrderDetailForm(forms.ModelForm):
    time_slot_choices = [("0","Today"),
                        ("09","9 AM"),
                        ("10","10 AM"),
                        ("11","11 AM"),
                        ("12","12 PM"),
                        ("13","1 PM"),
                        ("14","2 PM"),
                        ("15","3 PM"),
                        ("16","4 PM"),
                        ("17","5 PM"),
                        ("18","6 PM")]
    dresses_list_choices = [(str(i.id),str(i.Dress_Name)) for i in DressesDetail.objects.all()]
    order_type_choices = [("Dry","Dry"),("Wash","Wash")]
    
    Order_date = forms.DateField(widget=forms.DateInput(attrs={"min_value":date.today(),"type":"date","initial_value":date.today(),"class":"form-control w-50"},),required=True)
    Time_Slot = forms.CharField(widget=forms.Select(attrs={"class":"form-control w-50"},choices=time_slot_choices),required=True)
    Dresses_List = forms.CharField(widget=forms.Select(attrs={"class":"form-control"},choices=dresses_list_choices), required=False)
    Order_type = forms.CharField(widget=forms.Select(attrs={"class":"form-control w-50"},choices=order_type_choices),required=True)
    Pickup_date = forms.SplitDateTimeField(widget=SplitDateTimeWidget(date_attrs={"min_value":date.today(),"type":"date","initial_value":date.today(),"class":"form-control"},time_attrs={"class":"form-control","type":"time","min_value":datetime.now().strptime('09:00', "%H:%M"),"max_value":datetime.now().strptime('18:00', "%H:%M"),"initial_value":datetime.now().strftime("%H:%M")}), required=True) 
    Coupon = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control w-75","placeholder":"Apply Coupon (Optional)"}),max_length=6, required=False,label="Apply Coupon")
    
    class Meta:
        model = OrderDetail
        fields = ("Order_date","Time_Slot","Order_type","Pickup_date","Coupon")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper = FormHelper()
        self.helper.form_id = 'LoginForm'
        self.helper.form_class = 'form'
        self.helper.form_method = 'post'
        self.helper.form_action = "/customer/"
        self.helper.layout = Layout(
            Row(Div(Div(HTML("<b class='col-3' for='Order_date'>{{order_form.Order_date.label}}</b>"),Div(HTML("{{order_form.Order_date}}"),css_class="col-8"),css_class="row text-muted px-2 display-6 fs-4 pb-3"),
                    Div(HTML("<b class='col-3' for='Time_Slot'>{{order_form.Time_Slot.label}}</b>"),Div(HTML("{{order_form.Time_Slot}}"),css_class="col-8"),css_class="row text-muted px-2 display-6 fs-4 pb-3"),
                    Div(HTML("<b class='col-3' for='Dresses_List'>{{order_form.Dresses_List.label}}</b>"),Div(Row(Div(HTML("{{order_form.Dresses_List}}"),css_class="col-4"),Div(HTML('<input name="quantity" id="quantity" class="form-control w-75" value="1" type="number">'),css_class="col-3"),Div(Submit('submit', 'Add'),css_class="col-2")),css_class="col-9"),css_class="row text-muted px-2 display-6 fs-4 pb-3"),
                    Div(HTML("<b class='col-3' for='Order_type'>{{order_form.Order_type.label}}</b>"),Div(HTML("{{order_form.Order_type}}"),css_class="col-8"),css_class="row text-muted px-2 display-6 fs-4 pb-3"),
                    Div(HTML("<b class='col-3' for='Pickup_date'>{{order_form.Pickup_date.label}}</b>"),Div(Row(Div(HTML("{{order_form.Pickup_date.subwidgets.0}}"),css_class="col-5"),Div(HTML("{{order_form.Pickup_date.subwidgets.1}}"),css_class="col-4")),css_class="col-9"),css_class="row text-muted px-2 display-6 fs-4 pb-3"),
                    Div(HTML("<b class='col-3' for='Coupon'>{{order_form.Coupon.label}}</b>"),Div(HTML("{{order_form.Coupon}}"),css_class="col-9"),css_class="row text-muted px-2 display-6 fs-4 pb-3")
                    ,css_class="col-7"),HTML('''{% if show%}<div class="col-4">
                            <div class="card card-body shadow">
                                <h5 class="card-title text-center m-2">Order</h5>
                                <div class="text-muted fs-6 display-6 py-1"><b>Date: </b>{{date}}</div>
                                <div class="text-muted fs-6 display-6 py-1"><b>Order Type: </b>{{type}}</div>
                                <div class="text-muted fs-6 display-6 py-1"><b>TimeSlot: </b>{{slot}}</div>
                                {% if show%}
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Dress_Type</th>
                                            <th>Quantity</th>
                                            <th>Cost</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {% for item in dress_list %}
                                        <tr>
                                            <td>{{item.Dress_Name}}</td>
                                            <td>{{item.quantity}}</td>
                                            <td>{{item.cost}}$</td>
                                        </tr>
                                        {% endfor %}
                                    </tbody>
                                </table>
                                {% endif %}
                                <div class="row">
                                    {% if hasCoupon%}
                                    <div class="col-7">
                                        <div class="text-muted fs-6 display-6 pb-3"><b>Coupon: </b>{{Coupon}}</div>
                                    </div>
                                    <div class="col">
                                        <div class="text-muted fs-6 display-6 pb-3 text-center"><b>Discount Cost:</b> {{coupon_cost}}$ </div>
                                    </div>
                                    {% endif %}
                                </div>
                                <div class="row">
                                    <div class="col-7">
                                        <div class="text-muted fs-6 display-6 pb-3"><b>PickUp: </b>{{pickup}}</div>
                                    </div>
                                    <div class="col">
                                        <div class="text-muted fs-6 display-6 pb-3 text-center"><b>Total Cost:</b> {{total}}$ </div>
                                    </div>
                                </div>

                                <form action="{% url 'CUSTOMER:Homepage'%}" method="POST">
                                    <input type="submit" class="btn btn-success " value="Book" name="Book">
                                </form>
                                </div>
                            </div>{% endif %}''')),
            
            )
 
            
        
        
    
