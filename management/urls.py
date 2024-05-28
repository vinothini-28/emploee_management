from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_employee, name='add_employee'),
    path('list/', views.view_employees, name='employee_view'),
    path('edit/<str:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<str:id>/', views.delete_employee, name='delete_employee'),  # URL pattern for delete_employee view
]
