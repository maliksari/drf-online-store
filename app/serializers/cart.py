from rest_framework import serializers
from app.models import Cart, CartItem, Product

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'count', 'price']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True,write_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'total_price', 'cart_items']

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)

        for item_data in cart_items_data:
            product_id = item_data['product'].id
            quantity = item_data['count']
            product = Product.objects.get(id=product_id)

            if not product.in_stock or product.amount_in_stock < quantity:
                raise serializers.ValidationError('Product is not in stock')

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.count += quantity
            cart_item.price = product.price * cart_item.count
            cart_item.save()

            cart.total_price += cart_item.price
            
            cart.save()

        return cart