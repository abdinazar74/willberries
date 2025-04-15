from .models import *
from rest_framework import serializers


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_image', 'category_name']

class SubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ['subcategories_name']

class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_category = SubcategoriesSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['category_name', 'sub_category']

class SubcategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ['id','subcategories_name']



class UserProfileOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name',]




class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_image']

class ProductListSerializer(serializers.ModelSerializer):
    category = SubcategoriesSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%y %H:%M'))
    owner = UserProfileSerializer()
    product_photos = ProductImageSerializer(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_photos', 'category', 'price',
                  'created_date', 'product_type', 'owner', 'avg_rating', 'count_review']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_review(self, obj):
        return obj.get_count_review()


class SubcategoriesDetailSerializer(serializers.ModelSerializer):
    sub_category_product = ProductListSerializer(read_only=True, many=True)

    class Meta:
        model = Subcategories
        fields = ['subcategories_name', 'sub_category_product']

class ReviewsSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%y %H:%M')
    author = UserProfileSerializer()

    class Meta:
        model = Reviews
        fields = ['author', 'text', 'stars', 'created_date']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = SubcategoriesSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%y %H:%M'))
    owner = UserProfileOwnerSerializer()
    product_photos = ProductImageSerializer(read_only=True, many=True)
    product_review = ReviewsSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_video','product_photos', 'category', 'price',
                  'created_date', 'product_type','article_number', 'description','owner','product_review']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


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

