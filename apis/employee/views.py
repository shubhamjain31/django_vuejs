from rest_framework.views import APIView
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import *

# Create your views here.

class RoleAPI(APIView):
    def get_object(self, _id):
        return Role.objects.get(pk=_id)

    def get(self, request, id=None, *args, **kwargs):
        try:
            if not id:
                all_roles = Role.objects.all()
                serializer = RoleSerializer(all_roles,  many=True)
            else:
                role_ = Role.objects.get(id=id)
                serializer = RoleSerializer(role_)
            
            return Response({
                    'status':   200,
                    'message': 'All Roles',
                    'data':     serializer.data
                })
            
        except Exception as e:
            print(e)

    def post(self, request):
        try:
            data = request.data
            serializer = RoleSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            return Response({
                'status':   200,
                'message': 'Role Created!',
                'data':     serializer.data
            })
            
        except Exception as e:
            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     serializer.data
            })

    def put(self, request, id=None, *args, **kwargs):
        try:
            data = request.data
            obj = self.get_object(id)
            serializer = RoleSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()

            return Response({
                'status':   200,
                'message': 'Role Updated!',
                'data':     serializer.data
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     serializer.data
            })

    def delete(self, request, id=None, *args, **kwargs):
        try:
            data = request.data
            obj = self.get_object(id)
            obj.delete()

            return Response({
                'status':   200,
                'message': 'Role Deleted!',
                'data':     data
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     {}
            })

class DepartmentAPI(APIView):
    def get_object(self, _id):
        return Department.objects.get(pk=_id)

    def get(self, request, id=None, *args, **kwargs):
        try:
            if not id:
                all_departments = Department.objects.all()
                serializer = DepartmentSerializer(all_departments,  many=True)
            else:
                role_ = Department.objects.get(id=id)
                serializer = DepartmentSerializer(role_)
            
            return Response({
                    'status':   200,
                    'message': 'All Departments',
                    'data':     serializer.data
                })
            
        except Exception as e:
            print(e)

    def post(self, request):
        try:
            data = request.data
            serializer = DepartmentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            return Response({
                'status':   200,
                'message': 'Department Created!',
                'data':     serializer.data
            })
            
        except Exception as e:
            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     serializer.data
            })

    def put(self, request, id=None, *args, **kwargs):
        try:
            data = request.data
            obj = self.get_object(id)
            serializer = DepartmentSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()

            return Response({
                'status':   200,
                'message': 'Department Updated!',
                'data':     serializer.data
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     serializer.data
            })

    def delete(self, request, id=None, *args, **kwargs):
        try:
            data = request.data
            obj = self.get_object(id)
            obj.delete()

            return Response({
                'status':   200,
                'message': 'Department Deleted!',
                'data':     data
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status':   400,
                'message': 'Something Went Wrong!',
                'data':     {}
            })

class EmployeeAPI(APIView):
    def get_object(self, _id):
        return Employee.objects.get(pk=_id)

    def get(self, request, id=None, *args, **kwargs):
        try:
            if not id:
                all_employees = Employee.objects.all()
                serializer = EmployeeSerializer(all_employees,  many=True)
            else:
                employee_ = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(employee_)
            
            return Response({
                    'status':   200,
                    'message': 'All Employees',
                    'data':     serializer.data
                })
            
        except Exception as e:
            print(e)