from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EmployeeForm
from .models import *


def listEmp():
    emps = Employee.objects.all()
    return emps


def createEmp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        messages.success(request, 'Employee added successfully!!!')
        form = EmployeeForm()
        return render(request, 'addEmp.html', {'form': form})
    else:
        form = EmployeeForm()
        return render(request, 'addEmp.html', {'form': form})


def empList(request):
    emps = listEmp()
    return render(request, 'empList.html', {'emps': emps})


def delEmp(request, id):
    emps = listEmp()
    emp = Employee.objects.get(pk=id)
    emp.delete()
    messages.error(request, "Employee deleted successfully!!")
    return render(request, 'empList.html', {'emps': emps})


def updateEmp(request, id):
    emp = Employee.objects.get(pk=id)
    form = EmployeeForm(request.POST or None, instance=emp)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Employee update successfully!!!")
            return redirect('list-emp')
    else:
        return render(request, 'addEmp.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')
