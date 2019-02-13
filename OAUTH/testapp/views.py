from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
class Employee_CRUD(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    authentication_classes=[BasicAuthentication,]
    permission_classes=[IsAuthenticated,]


# Create your views here.
