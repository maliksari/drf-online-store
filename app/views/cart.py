from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound, ValidationError, AuthenticationFailed
from decimal import Decimal

from app.models import Cart, CartItem, Order, Product
from app.serializers.cart import CartSerializer, CartItemSerializer
from app.serializers.order import OrderSerializer
from .base import Auth


class CreateCartView(Auth, APIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    @swagger_auto_schema(operation_description="Create Cart", request_body=CartSerializer, tags=['Cart'])
    def post(self, request):
        user = request.user

        serializer = CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        cart_items_data = validated_data.pop('cart_items')

        cart = Cart.objects.create(user=user)

        total_price = 0

        for item_data in cart_items_data:
            product_id = item_data['product'].id
            quantity = item_data['count']
            product = Product.objects.get(id=product_id)

            if not product.in_stock or product.amount_in_stock < quantity:
                raise ValidationError('Product is not in stock')

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.count += quantity
            cart_item.price = product.price * cart_item.count
            cart_item.save()

            total_price += cart_item.price

        cart.total_price = total_price
        print("---total",total_price,"***",cart_item.price)
        cart.save()

        return Response(serializer.data, status=201)