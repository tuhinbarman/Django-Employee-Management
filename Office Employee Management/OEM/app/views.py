from django.shortcuts import render,redirect

from .models import Role,Department,Employee

# Create your views here.

def index(request):
    return render(request,"home/index.html")


def add(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =  request.POST['last_name']
        dept_name = request.POST['department']
        dept = Department.objects.get(name = dept_name)
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role_name = request.POST['role']
        role = Role.objects.get(name = role_name)
        phone = request.POST['phone']
        hire_date = request.POST['hire_date']
        employee = Employee(first_name= first_name,last_name=last_name,
                            dept=dept,salary=salary,bonus=bonus,
                            role=role,phone=phone,hire_date=hire_date)
        employee.save()
        return redirect('index')
    else:
        roles = Role.objects.all()
        departments = Department.objects.all()
        context = {
            'roles' : roles,
            'departments' : departments
        }
        return render(request,"home/add.html",context)

def list(request):
    list = Employee.objects.all()
    context = {
        'list' : list
    }
    return render(request,"home/list.html",context)

def delete(request,id):
    if request.method == 'POST':
        item = Employee.objects.get(id=id)
        item.delete()
        return redirect('list')


def update(request,id):
    if request.method == 'POST' :
        employee = Employee.objects.get(id=id)
        employee.last_name = request.POST['last_name']
        employee.first_name = request.POST['first_name'] 
        dept = request.POST['department']
        employee.dept = Department.objects.get(id = dept)
        employee.salary = request.POST['salary']
        employee.bonus = request.POST['bonus']
        role = request.POST['role']
        employee.role = Role.objects.get(id = role)
        employee.phone = request.POST['phone']
        employee.hire_date = request.POST['hire_date']
        employee.save()
        return redirect('list')
    else:
    
        item = Employee.objects.get(id=id)
        roles = Role.objects.all()
        departments = Department.objects.all()
        context = {
            'item' : item,
            'roles' : roles,
            'departments' : departments
        }
        return render(request,"home/update.html",context)
