"""auth URL Configuration

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
from django.urls import path,re_path,include
from rest_framework import routers
from testapp import views
router=routers.DefaultRouter()
router.register('get-api',views.Employee_CRUD)
router.register('',views.Employee_CRUD)
from rest_framework.authtoken import views as v
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/', include(router.urls)),
    #re_path(r'^get-api/',v.obtain_auth_token,name='get'),
    re_path('^auth-jwt/',obtain_jwt_token),
    re_path('^auth-jwt-refresh/',refresh_jwt_token),
    re_path('^auth-jwt-verify/',verify_jwt_token),


]
