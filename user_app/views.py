from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        # data is in object format.
        data = request.data
        # serialize the given user with our serializer
        # we pass the data into the serializer create method written in serializer

        # This is happens behind the scene
        # serializer = UserCreateSerializer(
        #     data={
        #         "first_data": data["first_name"],
        #         "last_name": data["last_name"],
        #         "email": data["email"],
        #         "password": data["password"],
        #     }
        # )
        serializer = UserCreateSerializer(data=data)

        # Now user objects has a property data it will return as Response
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetriveUserView(APIView):
    # only authenticted user call this api
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
