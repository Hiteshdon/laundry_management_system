from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.
class URlTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.homepage = "employee:Homepage"
        self.machine_status = "employee:Machine Status"
        self.invertory = "employee:Inventory"
        self.add_supply = "employee:Add Supply"
    
    def test_homepage_GET(self):
        response = self.client.get(reverse(self.homepage))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'employee\dashboard.html')
    
    
    def test_status_GET(self):
        response = self.client.get(reverse(self.machine_status))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'employee\status.html') 
    
    
    def test_invetory_GET(self):
        response = self.client.get(reverse(self.invertory))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'employee\inventory.html') 
    
    
    def test_invetory_GET2(self):
        response = self.client.get(reverse(self.add_supply,args={1}))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'employee\inventory.html') 
    

