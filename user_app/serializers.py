from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    # ModelSerializer used to validate data itself.
    class Meta:
        model = User
        # we can choose specific instead of entire field with a tuple
        fields = ("first_name", "last_name", "email", "password")

    # password validation for improving security
    def validate(self, data):
        # create instance with the given data
        user = User(**data)
        password = user.password
        try:
            validate_password(password, user)
        # validate perticular exception
        except exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {"password error": serializer_error.get("non_field_errors", [])}
            )

    # we are overriding the create.

    # validated data comes from RegisterView data={}
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


# UserCreateSerializer it will display the password in it's responce
# Creating another serializer for providing responce without password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # avoid the password field we can use this serializer to provide responce
        fields = ("first_name", "last_name", "email")
