from rest_framework import generics

from app.serializers.users import CreateUserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
