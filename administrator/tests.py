from re import S
from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.

class UrlTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.homepage = "admins:Homepage"
        self.customers_details = "admins:Customers-Details"
        self.customer_details = "admins:Customer-Details"
        self.employees_details = "admins:Employees-Details"
        self.employee_details = "admins:Employee-Details"
    
    def test_homepage(self):
        response = self.client.get(reverse(self.homepage))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'administrator\dashboard.html') 
    
    def test_customers(self):
        response = self.client.get(reverse(self.customers_details))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'administrator\customer.html') 
    
    def test_customer(self):
        response = self.client.get(reverse(self.customer_details,args={2}))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'administrator\customer.html') 
    
    def test_employees(self):
        response = self.client.get(reverse(self.employees_details))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'administrator\employee.html') 
    
    def test_employee(self):
        response = self.client.get(reverse(self.employee_details,args={7}))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'administrator\employee.html') 
        