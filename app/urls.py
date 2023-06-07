from django.urls import path
from rest_framework import routers

from .views import category, users, product, cart, redis_test
from .test_view import test_celery


router = routers.DefaultRouter()

router.register(r'category', category.CategoryView, basename='category')

urlpatterns = [
    path('register/', users.CreateUserView.as_view(),
         name="register"),
    path('categories/<int:category_id>/products/',
         category.CategoryProductsAPIView.as_view(), name='category-products'),
    path('products/', product.ProductView.as_view(),
         name='product'),
    path('products/<int:pk>/', product.ProductDetailView.as_view(),
         name='product-detail'),

    path('cart/', cart.CreateCartView.as_view(),
         name='create-cart'),
    path('cart/<int:pk>/completed', cart.CartCopmletedView.as_view(),
         name='completed-cart'),

    path('user/<int:pk>/cart', users.UserCartAPIView.as_view(),
         name='user-cart'),
    path('redis', redis_test.RedisView.as_view(), name="redis"),
    path('rabbit/test', test_celery, name="rabbitmq")

]

urlpatterns += router.urls
