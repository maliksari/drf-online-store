from rest_framework import serializers

from app.models import Product, Category
# from app.serializers.category import CategorySerializer


class ProductCreateSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all())
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_code', 'description', 'image','amount_in_stock',
                  'price', 'in_stock', 'categories']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        product = Product.objects.create(**validated_data)
        for category in categories_data:
            product.categories.add(category)
        return product

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['categories'] = instance.categories.values_list('id', flat=True)
        return ret


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_code', 'description','image',
                  'amount_in_stock', 'price', 'in_stock')
