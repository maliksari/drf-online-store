from rest_framework import serializers

from app.models import CustomUser
from app.models import Product, Cart, CartItem


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'role', 'is_active', 'password')
        # write_only_fields = ('password',)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class CartItemSerializer(serializers.ModelSerializer):
    product = UserProductSerializer()

    class Meta:
        model = CartItem
        fields = ('product', 'count', 'price')


class UserCartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    cartitem_set = CartItemSerializer(many=True, source='cartitem_set.all')

    class Meta:
        model = Cart
        fields = ("id", 'user_id', 'total_price', 'cartitem_set')
