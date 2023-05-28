from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound, ValidationError, AuthenticationFailed
from decimal import Decimal

from app.models import Cart, CartItem, Order, Product
from app.serializers.cart import CartItemSerializer, CartSerializer, CartCompletedSerializer
from app.serializers.order import OrderSerializer
from .base import Auth


class CreateCartView(Auth, APIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    @swagger_auto_schema(operation_description="Create Cart", request_body=CartSerializer, tags=['Cart'])
    def post(self, request):
        user = request.user
        data = request.data
        serializer = CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        print("*****///", validated_data.get('cart_items'))

        cart = Cart.objects.filter(
            user=user, is_active=True, is_completed=False).exists()

        # print("*****", cart.user_id, cart.pk, cart.is_completed)
        # cart varmı yokmu
        if not cart:
            cart = Cart.objects.create(user=user)

        cart_items_data = data.get('cart_items')

        total_price = 0

        for item_data in cart_items_data:
            product_id = item_data['product']
            quantity = item_data['count']
            product = Product.objects.get(id=product_id)

            if not product.in_stock or product.amount_in_stock < quantity:
                raise ValidationError('Product is not in stock')

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product)
            cart_item.count += quantity
            cart_item.price = product.price * quantity
            cart_item.save()

            total_price += cart_item.price

        cart.total_price = total_price
        print("---total", total_price, "***", cart_item.price)
        response = {
            "total_price": total_price,
            "products": CartItemSerializer(CartItem.objects.filter(cart=cart, is_active=True), many=True).data
        }

        cart.save()

        return Response(response, status=201)


class CartCopmletedView(Auth, APIView):
    serializer_class = CartSerializer
    # queryset = Cart.objects.all()

    @swagger_auto_schema(operation_description="Cart completed", request_body=CartCompletedSerializer, tags=['Cart'])
    def patch(self, request, pk):
        data = request.data

        try:
            cart = Cart.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"message": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartCompletedSerializer(cart, data=data, partial=True)

        if serializer.is_valid():
            cart.is_completed = data['is_completed']
            cart.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
