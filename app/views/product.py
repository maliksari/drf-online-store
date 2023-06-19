from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser


from app.models import Product
from app.serializers.product import ProductCreateSerializer, ProductSerializer
from common.utils import delete_cache


class ProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (FormParser, MultiPartParser)

    CACHE_KEY_PREFIX = "products-view"

    @swagger_auto_schema(operation_description="Product list", tags=['Product'])
    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def get(self, request):
        queryset = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Product create", request_body=ProductCreateSerializer, tags=['Product'])
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            delete_cache(self.CACHE_KEY_PREFIX)

            return Response({
                "data": serializer.data
            })
        else:
            return Response({
                "errors": serializer.errors
            })


class ProductDetailView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    CACHE_KEY_PREFIX = "products-detail-view"

    @swagger_auto_schema(operation_description="Product detail", tags=['Product'])
    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Product delete", tags=['Product'])
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            delete_cache(self.CACHE_KEY_PREFIX)
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Product update", request_body=ProductSerializer, tags=['Product'])
    def put(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data
        serializer = ProductSerializer(
            instance=product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            delete_cache(self.CACHE_KEY_PREFIX)
        return Response({"message": "Product updated successfully"}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Product patch", request_body=ProductSerializer, tags=['Product'])
    def patch(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data
        serializer = ProductSerializer(
            instance=product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            delete_cache(self.CACHE_KEY_PREFIX)
        return Response({"message": "Product updated successfully"}, status=status.HTTP_200_OK)
