from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    # ModelSerializer used to validate data itself.
    class Meta:
        model = User
        fields = "__all__"
