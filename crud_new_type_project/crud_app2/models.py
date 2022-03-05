from django.db import models

# Create your models here.
class Employee_table(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    contact = models.CharField(max_length=10)
    department = models.CharField(max_length=70)
    emp_id = models.CharField(max_length=5)
    password = models.CharField(max_length=70)