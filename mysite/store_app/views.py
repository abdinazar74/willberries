from .models import *
from rest_framework import viewsets, generics
from .serializers import (
    UserProfileSerializer,CategoryListSerializer, SubcategoriesListSerializer, CategoryDetailSerializer,
    ProductDetailSerializer,ProductListSerializer,SubcategoriesDetailSerializer,ProductSerializer,
    ReviewsSerializer, CartSerializer, CartItemSerializer, FavoriteSerializer, FavoriteItemSerializer, ProductImageSerializer
)


class CategoryListAPIViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryDetailAPIViews(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ProductEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class SubcategoriesListAPIView(generics.ListAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesListSerializer

class SubcategoriesDetailAPIView(generics.RetrieveAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesDetailSerializer

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





