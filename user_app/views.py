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
        print("--------type of data ----------", data)
        # what happens behind the scene check LogicFile.py - line 4
        serializer = UserCreateSerializer(data=data)
        print("----- serializer ------", serializer)

        if serializer.is_valid():
            # creating object with serializer data
            user = serializer.create(serializer.validated_data)
            # serialize our user object with UserSerializer for hide password.
            user = UserSerializer(user)
            print("--------- user ---------", user)
            # Now user objects has a property data it will return as Response
            return Response(user.data, status=status.HTTP_201_CREATED)
        print("------------ exception ------------")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetriveUserView(APIView):
    # only authenticted user call this api
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # fetch the user from the sessin
        user = request.user
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)


class RetriveData(APIView):
    def get(self, request):
        data = {"data": "configuration success"}

        return Response(data, status=status.HTTP_200_OK)
