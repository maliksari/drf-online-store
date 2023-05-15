from django.urls import path
from rest_framework import routers

from .views import category, users,product,cart


router = routers.DefaultRouter()
# router.register(r'product', product.ProductView, basename='product')
router.register(r'category', category.CategoryView, basename='category')

urlpatterns = [
    path('register/', users.CreateUserView.as_view(),
         name="register"),
    path('categories/<int:category_id>/products/', category.CategoryProductsAPIView.as_view(), name='category-products'),
    path('products/', product.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', product.ProductRetrieveUpdateDeleteView.as_view(),
         name='product-retrieve'),
    
#     path('cart/', cart.CreateCartView.as_view(),
#          name='create-cart'),
    
#     path('cart/<int:pk>/', cart.CartAPIView.as_view(),
#          name='cart-retrieve'),

]

urlpatterns += router.urls
