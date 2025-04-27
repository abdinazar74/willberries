

from django.urls import path, include
from .views import (
    UserProfileViewSets, CategoryListAPIViews,
    SubcategoriesListAPIView, SubcategoriesDetailAPIView, CategoryDetailAPIViews,
    ProductListAPIView, ProductDetailAPIView, ProductDetailAPIView,RegisterView,CustomLoginView,LogoutView,
    ReviewsViewSets, CartViewSets, CartItemViewSets,ProductEditAPIView,
    FavoriteViewSets, FavoriteItemViewSets, ProductCreateAPIView
)
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSets, basename='users' )




urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('products/create/<int:pk>', ProductEditAPIView.as_view(), name='product_edit'),
    path('category/', CategoryListAPIViews.as_view(), name= 'category_list'),
    path('category/<int:pk>/', CategoryDetailAPIViews.as_view(), name='category_detail'),
    path('sub-category/', SubcategoriesListAPIView.as_view(), name='sub_category_list'),
    path('sub-category/<int:pk>/', SubcategoriesDetailAPIView.as_view(), name='sub_category_detail'),
    path('cart/', CartViewSets.as_view(), name='cart_detail'),
    path('cart_items/', CartItemViewSets.as_view({'get': 'list', 'post': 'create'} )),
    path('cart_items/<int:pk>', CartItemViewSets.as_view({'put': 'update', 'delete': 'destroy'})),

]
