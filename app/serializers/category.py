from rest_framework import serializers

from app.models import Category
from app.serializers.product import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'category_code', 'description')


class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'category_code', 'description', 'products')
