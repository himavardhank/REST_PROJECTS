from rest_framework import serializers
from testapp2.models import Employee

def multiples_of_1000(value):
    	if value % 1000 !=0:
    		raise serializers.ValidationError("Salary should be multiple of 1000")
def validate(self, data):
    	ename = data.get('ename')
    	esal = data.get('esal')
    	if ename.lower() == 'Manu Mohan':
    		if esal < 60000:
    			raise serializers.ValidationError("Shankar salary minimum 60k")
    	return data

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
