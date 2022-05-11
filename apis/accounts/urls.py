from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('forget-password/', views.ForgetPasswordAPI.as_view(), name='forget-password'),

    path('users/', views.UserAPI.as_view(), name='users'),
    path('add-user/', views.UserAPI.as_view(), name='users'),
    path('get-user/<int:id>', views.UserAPI.as_view(), name='users'),
    path('edit-user/<int:id>', views.UserAPI.as_view(), name='users')
]
