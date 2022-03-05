from django import forms
from django.forms import fields, widgets
from .models import Employee_table

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee_table
        fields = ['name','email','contact','department','emp_id','password']
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name here..'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email-Id'}),
            'contact':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Department name'}),
            'emp_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Employee Id'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Strong Password..'}),
        }