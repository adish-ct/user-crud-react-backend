from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    # ModelSerializer used to validate data itself.
    class Meta:
        model = User
        # we can choose specific instead of entire field with a tuple
        fields = ("first_name", "last_name", "email", "password")

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
