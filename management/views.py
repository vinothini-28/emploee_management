from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Employee
from django.http import HttpResponse

def index(request):
    return render(request,'employee_details.html')

def add_employee(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        branch = request.POST.get('branch')
        contact = request.POST.get('contact')
        department = request.POST.get('department')

        # Create and save the new employee
        Employee.objects.create(
            id=id,
            firstname=firstname,
            email=email,
            dob=dob,
            branch=branch,
            contact=contact,
            department=department,
        )
        return redirect('employee_view')  # Redirect to the employee list view
    
    return render(request, 'employee_add.html')

def view_employees(request):
    query = request.GET.get('q')
    if query:
        employee_list = Employee.objects.filter(firstname__icontains=query) | Employee.objects.filter(email__icontains=query) | Employee.objects.filter(id__icontains=query)
    else:
        employee_list = Employee.objects.all()
    
    paginator = Paginator(employee_list, 5)  # Show 10 employees per page

    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page.

    return render(request, 'employee_view.html', {'employees': employees, 'query': query})

def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.firstname = request.POST.get('firstname')
        employee.email = request.POST.get('email')
        employee.dob = request.POST.get('dob')
        employee.branch = request.POST.get('branch')
        employee.contact = request.POST.get('contact')
        employee.department = request.POST.get('department')
        employee.save()
        return redirect('employee_view')
    
    return render(request, 'employee_update.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_view')
    
    return redirect('employee_view')  # Redirect to the employee list view after deletion
