from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from app.models import CustomUser, Cart
from app.serializers.users import CreateUserSerializer, UserCartSerializer
from .base import Auth


class CreateUserView(Auth, generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class UserCartAPIView(Auth, APIView):

    @swagger_auto_schema(operation_description="User Cart", tags=['Cart'])
    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(id=pk)
            cart = Cart.objects.filter(
                user=user, is_completed=False).latest('created_on')
            serializer = UserCartSerializer(cart)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=404)
        except Cart.DoesNotExist:
            return Response({"error": "Cart does not exist"}, status=404)
