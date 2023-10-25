#  Added logic in this file

# First logic - 1.
#  user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
#  serialize = UserCreateSerializer(user)

# First logic - updated, create function implemented serializers.py and create without the help of User model.
# serializer = UserCreateSerializer(
#     data={
#         "first_data": data["first_name"],
#         "last_name": data["last_name"],
#         "email": data["email"],
#         "password": data["password"],
#     }
# )
