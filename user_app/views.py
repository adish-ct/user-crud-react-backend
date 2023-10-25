from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):
    def post(self, request):
        data = request.data

        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        return Response({}, status=status.HTTP_201_CREATED)


class RetriveUserView(APIView):
    # only authenticted user call this api
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
