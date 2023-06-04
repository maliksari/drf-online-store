import logging

from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema


from app.models import Category
from app.serializers.category import CategoryProductSerializer, CategorySerializer
from common.utils import delete_cache

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    CACHE_KEY_PREFIX = "categories-view"

    @swagger_auto_schema(operation_description="Category list", tags=['Category'])
    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Category cerate", request_body=CategorySerializer,tags=['Category'])
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        delete_cache("categories-product")
        return response

    @swagger_auto_schema(operation_description="Category delete",tags=['Category'])
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response
    
    @swagger_auto_schema(operation_description="Category patch",tags=['Category'])
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response
    
    @swagger_auto_schema(operation_description="Category get",tags=['Category'])
    @method_decorator(cache_page(300, key_prefix=f"{CACHE_KEY_PREFIX}:id"))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Category put",tags=['Category'])
    def update(self, request, *args, **kwargs):
        delete_cache(self.CACHE_KEY_PREFIX)
        return super().update(request, *args, **kwargs)
    

class CategoryProductsAPIView(generics.RetrieveAPIView):
    serializer_class = CategoryProductSerializer
    lookup_field = 'id'
    CACHE_KEY_PREFIX = "categories-product"

    @swagger_auto_schema(operation_description="Category Products",tags=['Category'])
    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def get(self, request, category_id):
        try:
            category = Category.objects.prefetch_related('products').get(id=category_id)
            serializer = self.serializer_class(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            raise NotFound('Category not found')
