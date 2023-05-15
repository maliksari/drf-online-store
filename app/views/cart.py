from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound, ValidationError, AuthenticationFailed

from app.models import Cart, CartItem, Order, Product
from app.serializers.cart import CartSerializer, CartItemSerializer
from app.serializers.order import OrderSerializer


# class CartAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CartSerializer
#     queryset = Cart.objects.all()

#     def get_object(self):
#         user = self.request.user
#         cart = Cart.objects.filter(user=user, is_completed=False).first()
#         if cart is None:
#             cart = Cart.objects.create(user=user)
#         return cart

#     def put(self, request, *args, **kwargs):
#         product_id = request.data.get('product_id')
#         count = request.data.get('count')
#         cart = self.get_object()
#         cart_item = get_object_or_404(
#             CartItem, cart=cart, product_id=product_id)
#         cart_item.count = count
#         cart_item.save()
#         serializer = self.get_serializer(cart)
#         return Response(serializer.data)


# class CreateCartView(APIView):

#     @swagger_auto_schema(operation_description="Create Cart",
#                          request_body=CartSerializer, tags=['Cart'])
#     def post(self, request):
#         user = request.user
#         if not user.is_authenticated:
#             raise AuthenticationFailed('User must be authenticated')

#         product_id = request.data.get('product_id')
#         quantity = request.data.get('quantity')
#         if not product_id or not quantity:
#             raise ValidationError('Product id and quantity are required')

#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             raise NotFound('Product not found')

#         if not product.in_stock or product.amount_in_stock < quantity:
#             raise ValidationError('Product is not in stock')

#         cart, created = Cart.objects.get_or_create(user=user)

#         cart_item, created = CartItem.objects.get_or_create(
#             cart=cart, product=product)

#         cart_item.count += quantity
#         cart_item.price = product.price * cart_item.count
#         cart_item.save()

#         cart.total_price += cart_item.price
#         cart.save()

#         serializer = CartSerializer(cart)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
