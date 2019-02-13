from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIo(json_data)
        data=JSONParser.parse(stream)
        id=data.get['id',None]
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

# Create your views here.
