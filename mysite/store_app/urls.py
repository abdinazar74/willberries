

from django.urls import path, include
from .views import (
      UserProfileViewSets, CategoryViewSets, SubcategoriesViewSets, ProductListAPIView,ProductDetailAPIView,
      ReviewsViewSets, CartViewSets, CartItemViewSets, FavoriteViewSets, FavoriteItemViewSets
)
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSets, basename='users' )
router.register(r'category', CategoryViewSets, basename='categories' )
router.register(r'sub-category', SubcategoriesViewSets, basename='sub-categories' )

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail')

]
