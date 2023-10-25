from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        # data is in object format.
        data = request.data

        # what happens behind the scene check LogicFile.py - line 4
        serializer = UserCreateSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # creating object with serializer data
        user = serializer.create(serializer.validated_data)
        # serialize our user object with UserSerializer for hide password.
        user = UserSerializer(user)
        # Now user objects has a property data it will return as Response
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetriveUserView(APIView):
    # only authenticted user call this api
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
