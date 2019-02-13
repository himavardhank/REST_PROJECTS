from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import TokenAuthentication
from testapp.permissions import IsReadOnly,Permission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from testapp.authentications import CustomAuthentication
from rest_framework.authentication import BasicAuthentication
class Employee_CRUD(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    authentication_classes=[BasicAuthentication,]
    permission_classes=[IsAuthenticated,]


# Create your views here.
