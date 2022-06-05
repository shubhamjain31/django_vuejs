from django.urls import path
from employee import views

urlpatterns = [
    path('roles/', views.RoleAPI.as_view(), name='roles'),
    path('add-role/', views.RoleAPI.as_view(), name='roles'),
    path('get-role/<int:id>', views.RoleAPI.as_view(), name='roles'),
    path('edit-role/<int:id>', views.RoleAPI.as_view(), name='roles'),
    path('delete-role/<int:id>', views.RoleAPI.as_view(), name='roles'),

    path('employees/', views.EmployeeAPI.as_view(), name='employees'),
]
