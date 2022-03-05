from django.shortcuts import redirect, render
from .models import Employee_table
from .forms import Employee_form
from django.contrib import messages
# Create your views here.

def home_page(request):
    return render(request, 'crud/home.html')

def add_data(request):
    if request.method=='POST':
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Add successfully!!!')
            form = Employee_form()
    else:
        form = Employee_form()
    return render(request, 'crud/add.html',{'form':form})

def show_data(request):
    stud = Employee_table.objects.all()
    return render(request, 'crud/show.html',{'stu':stud})

def update_data(request, id):
    if request.method == 'POST':
        pi = Employee_table.objects.get(pk=id)
        form = Employee_form(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request,'Form Updated successfully')
    else:
        pi = Employee_table.objects.get(pk=id)
        form = Employee_form(instance=pi)
    return render(request, 'crud/update.html',{'form':form})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Employee_table.objects.get(pk=id)
        pi.delete()
        return redirect('/show/')

def search_data(request):
    given = request.POST['name']
    emp = Employee_table.objects.filter(name__iexact=given)
    return render(request, 'crud/show.html',{'stu':emp})