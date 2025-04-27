from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                     MaxValueValidator(70)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('simple', 'simple'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_image = models.FileField(upload_to='category_icons/')
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Subcategories(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    subcategories_name = models.CharField(max_length=46, unique=True)

    def __str__(self):
        return f'{self.category} - {self.subcategories_name}'


class Product(models.Model):
    category = models.ForeignKey(Subcategories, on_delete=models.CASCADE, related_name='sub_category_product')
    product_name = models.CharField(max_length=65)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    article_number = models.PositiveIntegerField(unique=True)
    description = models.TextField()
    product_type = models.BooleanField(default=False)
    product_video = models.FileField(upload_to='product_videos/', null=True, blank=True)
    price = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_avg_rating(self):
        rating = self.product_review.all()
        if rating.exists():
            return round(sum([i.stars for i in rating]) / rating.count(), 1)
        return 0

    def get_count_review(self):
        return self.product_review.count()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photos')
    product_image =models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.product}, {self.product_image}'



class Reviews(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}'

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        return sum([i.get_total_price()for i in self.items.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product}, {self.quantity}'

    def get_total_price(self):
        return self.quantity * self.product.price

class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'




