from django.urls import path
from employee import views

urlpatterns = [
    path('employees/', views.EmployeeAPI.as_view(), name='employees'),
]
