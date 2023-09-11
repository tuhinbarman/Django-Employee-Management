from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    dept = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete = models.DO_NOTHING)
    phone = models.IntegerField(default = 0)
    hire_date = models.DateField()


