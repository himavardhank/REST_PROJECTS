from django.conf.urls import url,include
from rest_framework import routers
from testapp.api.views import HydJobsCRUDCBV
router=routers.DefaultRouter()
router.register('hydjobsinfo',HydJobsCRUDCBV)
urlpatterns = [
    url(r'', include(router.urls)),
]
