from .models import *
from rest_framework import viewsets, generics
from .serializers import (
    UserProfileSerializer,CategorySerializer, SubcategoriesSerializer, ProductDetailSerializer,ProductListSerializer,
    ReviewsSerializer, CartSerializer, CartItemSerializer, FavoriteSerializer, FavoriteItemSerializer, ProductImageSerializer
)


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = CategorySerializer

class SubcategoriesViewSets(viewsets.ModelViewSet):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer

class ProductImageViewSets(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ReviewsViewSets(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class CartViewSets(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSets(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class FavoriteViewSets(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteItemViewSets(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer





