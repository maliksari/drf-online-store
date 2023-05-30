from rest_framework import serializers
from app.models import CartItem, Product


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    count = serializers.IntegerField(label="Miktar")

    class Meta:
        model = CartItem
        fields = ('product', 'count')


class CartSerializer(serializers.Serializer):
    cart_items = CartItemSerializer(many=True)


class CartCompletedSerializer(serializers.Serializer):
    is_completed = serializers.BooleanField(label="Sepeti onayla")
