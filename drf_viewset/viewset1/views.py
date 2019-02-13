from django.shortcuts import render
from viewset1.models import Employee
from viewset1.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
class Employee_CRUD(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    
# Create your views here.
