from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

def welcome(request):
    return render(request, 'welcom.html')

def load_form(request):
    form = EmployeeForm
    return render(request,'index.html' ,{'form':form})

def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/showData')
    
def showData(request):
    employee = Employee.objects.all
    return render(request, 'showData.html' ,{'employee':employee})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html' ,{'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/showData')

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/showData')

def search(request):
    given_name = request.POST['name']
    employee = Employee.objects.filter(ename__icontains = given_name)
    return render(request,'showData.html',{'employee':employee})