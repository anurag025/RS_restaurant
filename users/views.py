from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Create your views here.
from users.models import EmployeeSerializer


class AddUser(APIView):

    def post(self, request):
        from menu.models import MenuSerializer
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')

        item = EmployeeSerializer(name=name, phone=phone, email=email)
        if item.is_valid():
            item.save()
            return Response({"data": {"msg": "item added succesfully", 'data': item.data}}, status=HTTP_200_OK)
        else:
            return Response(item.errors, status=HTTP_400_BAD_REQUEST)