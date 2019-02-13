from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apiview1.serializers import NameSerializer
from apiview1.models import Employee
class Testapiview(APIView):
    def get(self,request,format=None):
        colors=['white','white','green','yellow']
        return Response({'msg':'wish you happy new year','colors':colors})
    def post(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            msg='hello {} wish you happy new year!!!!'.format(serializer.data.get('name'))
            return Response({'msg':msg})
        return Response(Serializer.errors,status=400)
    def put(self,request,pk=None):
        return Response({'msg':'response from put method'})
    def patch(self,request,pk=None):
        return Response({'msg':'response from patch method'})
    def delete(self,request,pk=None):
        return Response({'msg':'response from delete method'})

from rest_framework import viewsets
class TestViewSet(viewsets.ViewSet):
    def list(self,request):
        colors=['red','white','green','yellow']
        return Response({'msg':'wish you happy new year welcome to 2019','colors':colors})


    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            msg='hello {} wish you happy new year!!!!'.format(serializer.data.get('name'))
            return Response({'msg':msg})
        return Response(Serializer.errors,status=400)

    def retrieve(self,request,pk=None):
        return Response({'msg','Response from retrieve method'})

    def update(self,request,pk=None):
        return Response({'msg','Response from update method'})

    def partial_update(self,request,pk=None):
        return Response({'msg','Response from paartial_update method'})

    def destroy(self,request,pk=None):
        return Response({'msg','Response from destroy method'})

from apiview1.serializers import EmployeeSerializer
class EmployeeListApiView(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        print(qs)
        Serializer=EmployeeSerializer(qs,many=True

        )
        #print(Serializer)
        #print(Serializer.data)
        return Response(Serializer.data)


from rest_framework import generics
class EmployeeAPIVIEW(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeSEARCHVIEW(generics.ListAPIView):
    #queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs

class EmployeeCREATEAPIVIEW(generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeDETAILAPIVIEW(generics.RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='eno'

class EmployeeUPDATEAPIVIEW(generics.UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

class EmployeeDELETEAPIVIEW(generics.DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

class EmployeeLISTCREATEAPIVIEW(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeRETRIEVEUPDATEAPIVIEW(generics.RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'


class EmployeeRETRIEVEDESTROYAPIVIEW(generics.RetrieveDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

class EmployeeRETRIEVEUPDATEDESTROYAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'



from rest_framework import mixins
class Employeelist_Model_Mixin(mixins.CreateModelMixin,generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class Employee_detailapi_Model_Mixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)




class All(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset=Employee.objects.all
    #print(queryset)
    serializer_class=EmployeeSerializer
    lookup_field='eno'
#
# class CRUD(generics.ListAPIView,generics.CreateAPIView,generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field="eno"

# Create your views here.
