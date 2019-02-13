from django.contrib import admin
from viewset1.models import Employee,Student
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','sno','sname','smarks','saddr']

admin.site.register(Employee,EmployeeAdmin,StudentAdmin)
# Register your models here.
