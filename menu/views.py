from django.shortcuts import render
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView


class AddItem(APIView):

    def post(self, request):
        from menu.models import MenuSerializer
        name = request.data.get('name')
        price = request.data.get('price')
        description = request.data.get('description')

        item = MenuSerializer(data={'name': name, 'price': price, 'description': description})
        if item.is_valid():
            item.save()
            return Response({"data": {"msg": "item added succesfully", 'data': item.data}}, status=HTTP_200_OK)
        else:
            return Response(item.errors, status=HTTP_400_BAD_REQUEST)