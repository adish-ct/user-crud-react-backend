from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            print("--------type of data ----------", data)

            serializer = UserCreateSerializer(data=data)
            print("----- serializer ------", serializer)

            if serializer.is_valid():
                user = serializer.create(serializer.validated_data)
                user = UserSerializer(user)
                return Response(user.data, status=status.HTTP_201_CREATED)
            else:
                print(
                    "Serializer Errors:", serializer.errors
                )  # Add this line for debugging
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Error during registration:", str(e))  # Add this line for debugging
            return Response(
                {"detail": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RetriveUserView(APIView):
    # only authenticted user call this api
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # fetch the user from the sessin
        user = request.user
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)
