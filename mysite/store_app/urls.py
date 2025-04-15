

from django.urls import path, include
from .views import (
    UserProfileViewSets, CategoryListAPIViews,
    SubcategoriesListAPIView, SubcategoriesDetailAPIView, CategoryDetailAPIViews,
    ProductListAPIView, ProductDetailAPIView, ProductDetailAPIView,
    ReviewsViewSets, CartViewSets, CartItemViewSets,ProductEditAPIView,
    FavoriteViewSets, FavoriteItemViewSets, ProductCreateAPIView
)
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSets, basename='users' )




urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('products/create/<int:pk>', ProductEditAPIView.as_view(), name='product_edit'),
    path('category/', CategoryListAPIViews.as_view(), name= 'category_list'),
    path('category/<int:pk>/', CategoryDetailAPIViews.as_view(), name='category_detail'),
    path('sub-category/', SubcategoriesListAPIView.as_view(), name='sub_category_list'),
    path('sub-category/<int:pk>/', SubcategoriesDetailAPIView.as_view(), name='sub_category_detail'),

]
