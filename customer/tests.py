from pydoc import cli
from django.test import Client, TestCase
from django.urls import reverse

from customer.views import Other
from .models import OrderDetail,UserDetail,Coupon,FeedBack,DressesDetail

# Create your tests here.
class TestViews(TestCase):
    object = Other()
    def setUp(self):
        self.client = Client()
        self.homepage_other = '/'
        self.loginpage = "/login/"
        self.homepage = "CUSTOMER:Homepage"
        self.profile = "CUSTOMER:ProfilePage"
        self.orderHistory = "CUSTOMER:Order History"
        
    def test_homepage_other_GET(self): 
        response = self.client.get(self.homepage_other)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'customer\home.html')

    
    
    def test_homepage_other_POST(self):
        response = self.client.get(self.loginpage)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'customer\home.html')
    
    def test_homepage(self):
        response = self.client.get(reverse(self.homepage))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'customer\order.html')
    
    
    def test_profile(self):
        response = self.client.get(reverse(self.profile))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'customer\home.html')
    
    
    
    def test_ordersHistory(self):
        response = self.client.get(reverse(self.orderHistory))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'customer\home.html') 
    
    
