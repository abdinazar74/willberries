from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class SubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ['subcategories_name']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_image']

class ProductListSerializer(serializers.ModelSerializer):
    category = SubcategoriesSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%y %H:%M'))
    owner = OwnerSerializer()
    product_photos = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_photos', 'category', 'price',
                  'created_date', 'product_type', 'owner']

class ReviewsSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%y %H:%M')
    author = UserProfileSerializer()

    class Meta:
        model = Reviews
        fields = ['author', 'text', 'stars', 'created_date']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = SubcategoriesSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%y %H:%M'))
    owner = UserProfileSerializer()
    product_photos = ProductImageSerializer(read_only=True, many=True)
    product_review = ReviewsSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_video','product_photos', 'category', 'price',
                  'created_date', 'product_type','article_number', 'description','owner','product_review']





class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'

