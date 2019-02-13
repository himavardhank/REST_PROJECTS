"""drf_apiview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from apiview1 import views
from django.conf.urls import url,include
from rest_framework import routers
rout=routers.DefaultRouter()
rout.register('test',views.TestViewSet,basename='test')
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'api/',views.Testapiview.as_view()),
    #url(r'',include(rout.urls)),
    #url(r'apiview/',views.EmployeeListApiView.as_view()),
    #url(r'listapiview/',views.EmployeeAPIVIEW.as_view()),
    #url(r'search/',views.EmployeeSEARCHVIEW.as_view()),
    #url(r'create/',views.EmployeeCREATEAPIVIEW.as_view()),
    #url(r'retrieve/(?P<eno>\d+)/$',views.EmployeeDETAILAPIVIEW.as_view
    #url(r'update/(?P<id>\d+)/$',views.EmployeeUPDATEAPIVIEW.as_view()),
    #url(r'destroy/(?P<id>\d+)/$',views.EmployeeDELETEAPIVIEW.as_view()),
    #re_path('listcreate/$',views.EmployeeLISTCREATEAPIVIEW.as_view()),
    #re_path('retrieveupdate/(?P<id>\d+)/$',views.EmployeeRETRIEVEUPDATEAPIVIEW.as_view()),
    #re_path('retrievedestroy/(?P<id>\d+)/$',views.EmployeeRETRIEVEDESTROYAPIVIEW.as_view()),
    #re_path('retrieveupdatedestroy/(?P<pk>\d+)/$',views.EmployeeRETRIEVEUPDATEDESTROYAPIVIEW.as_view()),
    re_path('all/(?P<eno>\d+)/$',views.All.as_view()),
    #re_path('crud/(?P<eno>\d+)/$',views.CRUD.as_view()),
    #re_path('',views.Employeelist_Model_Mixin.as_view()),
    #re_path('api/(?P<pk>\d+)/$',views.Employee_detailapi_Model_Mixin.as_view()),

]
