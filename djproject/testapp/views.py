from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from testapp.models import *

# Create your views here.
def index(request):
    return render(request,'testapp/index1.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,25)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})

def blorejobs(request):
    return render(request,'testapp/blorejobs.html')

def punejobs(request):
    return render(request,'testapp/punejobs.html')

def chennaijobs(request):
    return render(request,'testapp/chennaijobs.html')
