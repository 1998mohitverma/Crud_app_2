from django.contrib import admin
from .models import Employee_table
# Register your models here.

@admin.register(Employee_table)
class Employee_admin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','department','emp_id','password']