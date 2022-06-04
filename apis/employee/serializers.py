from rest_framework  import serializers
from django.contrib.auth.models import User
from accounts.models import *
from accounts.serializers import *
from employee.models import Employee, Role, Department

class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = ['name', 'description']

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ['name', 'description']

class EmployeeSerializer(serializers.ModelSerializer):
    user_set        = UserSerializer(many=True)
    role_set        = RoleSerializer(many=True)
    department_set  = DepartmentSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['user_set', 'title', 'image', 'firstname', 'lastname', 'othername', 'sex', 'email', 'tel', 'bio', 'birthday', 'religion',
                'nationality', 'hometown', 'region', 'residence', 'address', 'education', 'lastwork', 'position', 'ssnitnumber', 'id',
                'tinnumber', 'department_set', 'role_set', 'startdate', 'employeetype', 'employeeid', 'dateissued', 'is_blocked', 'is_deleted'
                'created']