from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
        ('SALES', 'Sales'),
        ('OPS', 'Operations'),
    ]

    id = models.CharField(max_length=10, primary_key=True)
    firstname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    dob = models.DateField()
    branch = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return f"{self.firstname}"
