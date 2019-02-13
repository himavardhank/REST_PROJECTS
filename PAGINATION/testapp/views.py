from django.shortcuts import render
from testapp.serializers import NameSerializer
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from testapp.pagination import Mypagination,Mypagination2,Mypagination3
#class Employee_Pagination(generics.ListAPIView):
    #queryset=Employee.objects.all()
    #serializer_class=EmployeeSerializer
    #pagination_class=Mypagination3

# class EmployeeAPIVIEW(generics.ListAPIView):
#     serializer_class=EmployeeSerializer
#     print(serializer_class)
#     def get_queryset(self):
#         qs=Employee.objects.all()
#         name=self.request.GET.get('ename')
#         if name is not None:
#             qs=qs.filter(ename__icontains=name)
#         return qs


class EmployeeAPIVIEW(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #search_fields=('=eno','^ename')
    ordering_fields=('eno','esal')
