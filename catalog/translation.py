from modeltranslation.translator import translator, TranslationOptions
from .models import ProductMedia, Product, Category


class ProductTrans(TranslationOptions):
    fields = [
        'title',
        'article',
        'image',
        'description',
        'file',
    ]


class CategoryTrans(TranslationOptions):
    fields = [
        'title',
        'image',
        'description',
    ]


class ProductMediaTrans(TranslationOptions):
    fields = [
        'image',
        'iframe',
    ]


translator.register(Product, ProductTrans)
translator.register(ProductMedia, ProductMediaTrans)
translator.register(Category, CategoryTrans)
