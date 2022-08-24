from django.contrib import admin
from .models import Customers, Employees


# Register your models here.
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = [
        'customernumber',
        'customername',
        'contactlastname',
        'contactfirstname',
        'phone',
        'city',
        'state',
    ]


@admin.register(Employees)
class Employees(admin.ModelAdmin):
    list_display = ['employeenumber', 'lastname', 'firstname', 'email', 'jobtitle']
