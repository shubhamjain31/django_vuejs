from django.urls import path
from employee import views

urlpatterns = [
    path('roles/', views.RoleAPI.as_view(), name='roles'),
    path('add-role/', views.RoleAPI.as_view(), name='roles'),
    path('get-role/<int:id>', views.RoleAPI.as_view(), name='roles'),
    path('edit-role/<int:id>', views.RoleAPI.as_view(), name='roles'),
    path('delete-role/<int:id>', views.RoleAPI.as_view(), name='roles'),

    path('departments/', views.DepartmentAPI.as_view(), name='departments'),
    path('add-department/', views.DepartmentAPI.as_view(), name='departments'),
    path('get-department/<int:id>', views.DepartmentAPI.as_view(), name='departments'),
    path('edit-department/<int:id>', views.DepartmentAPI.as_view(), name='departments'),
    path('delete-department/<int:id>', views.DepartmentAPI.as_view(), name='departments'),

    path('employees/', views.EmployeeAPI.as_view(), name='employees'),
    path('add-employee/', views.EmployeeAPI.as_view(), name='employees'),
]
