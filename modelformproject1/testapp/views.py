from django.shortcuts import render
from testapp.models import Student
from testapp.forms import StudentForm

# Create your views here.
def student_input_view(request):
    markssubmitted=False
    name=''
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            form.save()
            markssubmitted=True
    form=StudentForm()
    return render(request,'testapp/input.html',{'form':form,'markssubmitted':markssubmitted,'name':name})
