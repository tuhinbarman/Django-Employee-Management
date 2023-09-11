from django.contrib import admin

from .models import Department,Role,Employee

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('id','name','location')
    list_display_links = ('id','name')
    list_editable = ('location',)
    list_search = ('name','location')
    list_per_page = 15 
    

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    list_search = ('name')
    list_per_page = 15 

class EmployeeAdmin(admin.ModelAdmin):
   
    list_display = ('id','first_name','last_name','dept','phone','role','hire_date')
    list_display_links = ('id','first_name','last_name')
    list_editable = ('phone',)
    list_search = ('first_name','last_name','role')
    list_per_page = 15


admin.site.register(Department,DepartmentAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Employee,EmployeeAdmin)
