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
        data = request.data

        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        # create user object with the given data, it will return user
        user = User.objects.create_user(first_name, last_name, email, password)
        # serialize the given user with our serializer
        user = UserCreateSerializer(user)

        # Now user objects has a property data it will return as Response
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetriveUserView(APIView):
    # only authenticted user call this api
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
