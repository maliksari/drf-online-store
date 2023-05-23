from rest_framework import serializers
from app.models import CartItem, Cart, Order, Product


class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'count','price']

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        product = Product.objects.get(id=product_id)
        validated_data['product'] = product
        cart_item = CartItem.objects.create(**validated_data)
        return cart_item


class CartSerializer(serializers.ModelSerializer):
    product = CartItemSerializer(many=False)

    class Meta:
        model = Cart
        fields = ['user', 'total_price', 'product']
