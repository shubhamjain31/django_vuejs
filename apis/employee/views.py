from rest_framework.views import APIView
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import *

# Create your views here.

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