from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


# serializers.py
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]

    def validate(self, data):
        # Validate individual fields here if needed
        # For example, you can check if email is unique
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError(
                {"email": ["Email address must be unique."]}
            )

        # Validate password using Django's password validation
        password = data.get("password")
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})

        return data

    def create(self, validated_data):
        # Custom create method if needed
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
