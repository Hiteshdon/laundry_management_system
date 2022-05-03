from django.shortcuts import render
from employee.models import Machines
# Create your views here.
class Home:
    
    def __init__(self,context = {"page":'manager/main.html'}) :
        self.context =context
        
    def homepage(self,request):
        machines = Machines.objects.all()
        if request.method == "POST":
            print(request.POST)
        new ={"machines":machines}
        new.update(self.context)
        return render(request,'manager\dashboard.html',new)

class Other(Home):
    
    def __init__(self, context={ "page": 'manager/main.html' }):
        super().__init__(context)
        
    def employeeDashboard(self,request):
        return render(request,'employee/dashboard.html',self.context)

    def employeeMachineStatus(self,request):
        return render(request,'employee/status.html',self.context)