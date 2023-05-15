import logging

from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet

from app.models import Category, Product
from app.serializers.category import CategoryProductSerializer, CategorySerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryProductsAPIView(generics.RetrieveAPIView):
    serializer_class = CategoryProductSerializer
    lookup_field = 'id'

    def get_object(self):
        category_id = self.kwargs.get('category_id')
        try:
            category = Category.objects.prefetch_related(
                'products').get(id=category_id)
            return category
        except Category.DoesNotExist:
            raise NotFound('Category not found')
