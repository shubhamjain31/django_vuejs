from rest_framework  import serializers
from django.contrib.auth.models import User
from accounts.models import *
from accounts.serializers import *
from employee.models import Employee, Role, Department, Nationality, Religion

class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = ['name', 'description', 'created', 'id']

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ['name', 'description', 'created', 'id']

class EmployeeSerializer(serializers.ModelSerializer):
    # user_set        = UserSerializer(many=True)
    # role_set        = RoleSerializer(many=True)
    # department_set  = DepartmentSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['title', 'image', 'firstname', 'lastname', 'othername', 'sex', 'email', 'tel', 'bio', 'birthday', 'religion',
                'nationality', 'hometown', 'region', 'residence', 'address', 'education', 'lastwork', 'position', 'ssnitnumber', 'id',
                'tinnumber', 'department', 'role', 'startdate', 'employeetype', 'employeeid', 'dateissued']

class NationalitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nationality
        fields = ['name', 'flag', 'created', 'updated']

class ReligionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Religion
        fields = ['name', 'description', 'created', 'updated']
