from rest_framework import viewsets
from testapp.models import hydjobs
from testapp.api.serializers import HydJobsSerializer
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=HydJobsSerializer
    queryset=hydjobs.objects.all()
