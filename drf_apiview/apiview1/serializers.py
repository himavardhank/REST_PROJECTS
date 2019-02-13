from rest_framework import serializers
class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)

from apiview1.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Employee
        fields='__all__'
