from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

# Create your views here.
from users.models import Employee, Permision
from rest_framework.views import APIView


class Dashboard(APIView):

    def get(self, request):
        permissions = Permision.objects.filter(user_id='1')
        permission_list = [permission.permissions for permission in permissions]
        if 'access_dashboard_page' not in permission_list:

            return Response({"data": {"msg": f"You dont have permision to access this page"}}, status=HTTP_400_BAD_REQUEST)
        else:
            Response({"data": {}}, status=HTTP_200_OK)


