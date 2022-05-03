
from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.
class UrlTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.homepage = "manager:Homepage"
        
    def test_homepage(self):
        response = self.client.get(reverse(self.homepage))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'manager\dashboard.html') 