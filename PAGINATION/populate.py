import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PAGINATION.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
f=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=f.name()
        fesal=randint(10000,20000)
        feaddr=f.city()
        emp_rec=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
populate(200)
