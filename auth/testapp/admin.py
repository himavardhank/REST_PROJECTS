from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']
# class StudentAdmin(admin.ModelAdmin):
#     list_display=['id','sno','sname','smarks','saddr']
# class EmpAndStudent(admin.ModelAdmin):
#     list_display=['id','sno','sname','smarks','saddr']
admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
