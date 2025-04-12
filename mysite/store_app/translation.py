from .models import Category, Subcategories, Product
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Subcategories)
class SubcategoriesTranslationOptions(TranslationOptions):
    fields = ('subcategories_name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name','description')

