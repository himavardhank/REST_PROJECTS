from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
import json
def employee_data_view(request):
    employee_data={'eno':100,'ename':'sunny','esal':1000,'eaddr':'hyd'}
    resp=employee_data
    return HttpResponse(resp)
def employee_data_jsonview(request):
    employee_data={'eno':100,'ename':'sunny','esal':1000,'eaddr':'hyd'}
    json_data=json.dumps(employee_data)
    return HttpResponse(json_data,content_type='application/json')
def employee_data_jsondirectview(request):
    employee_data={'eno':100,'ename':'sunny','esal':1000,'eaddr':'hyd'}
    return JsonResponse(employee_data)
class Jsoncbv(View):
    def get(self,request,*args,**kwargs):
        employee_data={'eno':100,'ename':'sunny','esal':1000,'eaddr':'hyd'}
        return JsonResponse(employee_data)
from rest1.mixins import JsonResponseMixin
class Jsoncbv2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        employee_data = {'eno': 100, 'ename': 'sunny', 'esal': 1000, 'eaddr': 'hyd'}
        return self.render_to_json_response(employee_data)
