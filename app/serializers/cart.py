from rest_framework import serializers
from app.models import Cart, CartItem, Product


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    count = serializers.IntegerField(label="Miktar")

    class Meta:
        model = CartItem
        fields = ('product', 'count')


class CartSerializer(serializers.Serializer):
    cart_items = CartItemSerializer(many=True)

    # class Meta:
    #     model = Cart
    #     fields = ('cartitem_set',)
