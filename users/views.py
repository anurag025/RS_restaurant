from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Create your views here.
from users.models import EmployeeSerializer, Employee
from rest_framework.views import APIView


class User(APIView):

    def post(self, request):
        name = request.data.get('employee_name')
        phone = request.data.get('phone')
        email = request.data.get('email')

        create_user = EmployeeSerializer(data={'name': name, "phone": phone, "email": email})
        if create_user.is_valid():
            create_user.save()
            return Response({"data": {"msg": "user added succesfully"}}, status=HTTP_200_OK)
        else:
            return Response({"data": {"msg": f"User with this phone {phone} number already exist"}},
                            status=HTTP_400_BAD_REQUEST)

        # employee, status = Employee.objects.get_or_create(name=name, email=email, phone=phone)
        # if not status:
        #     return Response({"data": {"msg": f"User with this phone {phone} number already exist"}}, status=HTTP_400_BAD_REQUEST)
        # else:
        #     return Response({"data": {"msg": "user added succesfully"}}, status=HTTP_200_OK)

