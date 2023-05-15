from rest_framework import serializers

from app.models import Order
from app.serializers.cart import CartItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'cart', 'status', 'created_at', 'cart_items']