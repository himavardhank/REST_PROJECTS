from django.shortcuts import render
from django.views.generic import View
from retrieveapp.models import Employee
import json
from django.http import HttpResponse
from retrieveapp.mixins import serialize_Mixins
from retrieveapp.utils import is_json
from retrieveapp.mixins import HttpResponseMixin


class EmployeeCRUD(View):
    def get(self,request,*args,**kwargs):
        emp=Employee.objects.get(id=1)
        data={
            'eno':emp.eno,
            'empname': emp.ename,
            'esal':emp.esal,
            'empaddrs':emp.eaddr,
        }
        json_data=json.dumps(data)
        return HttpResponse(json_data,content_type='application/json')


class EmployeeCRUD_Dynamic(View):
    def get(self, request, id,*args, **kwargs):
        emp = Employee.objects.get(id=id)
        data = {
            'eno': emp.eno,
            'empname': emp.ename,
            'esal': emp.esal,
            'empaddrs': emp.eaddr,
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

from django.core.serializers import serialize
class EmployeeCRUD_Serialize(View):
    def get(self, request, id,*args, **kwargs):
        emp = Employee.objects.get(id=id)
        json_data = serialize('json',[emp,],fields=('eno','ename'))
        return HttpResponse(json_data, content_type='application/json')

class EmployeeCRUD_all(View):
    def get(self, request,*args, **kwargs):
        qs= Employee.objects.all()
        json_data = serialize('json',qs)
        return HttpResponse(json_data, content_type='application/json')

class EmployeeCRUD_originaldata(View):
    def get(self, request,*args, **kwargs):
        qs= Employee.objects.all()
        json_data = serialize('json',qs)
        pdict=json.loads(json_data)
        final_list=[]
        for obj in pdict:
            final_list.append(obj['fields'])
        json_data=json.dumps(final_list)
        return HttpResponse(json_data, content_type='application/json')

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUD_Using_Mixins(HttpResponseMixin,serialize_Mixins,View):
    def get(self, request,*args, **kwargs):
        qs= Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
            return self.render_to_http_response(json.dumps({'msg':'please send valid data only'}),status=400)
            empdata=json.loads(request.body)
            form=EmployeeForm(empdata)
            json_data=json.dumps({'msg':'sucessfully created resource'})
        return self.render_to_http_response(json_data)

class EmployeeCRUD_Using_Mixins_Dynamic(HttpResponseMixin,serialize_Mixins,View):
    def get(self, request,id,*args, **kwargs):
        try:
            emp= Employee.objects.get(id=id)
        except Employee.DoesnotExist:
            json_data=json.dumps({'msg':'specified id is not exist'})
            return self.render_to_http_response(json_data,404)
        else:
            json_data=self.serialize([emp,])
            return HttpResponse(json_data,content_type='application/json')






# Create your views here.
