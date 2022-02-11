from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from .models import Category, Product, ProductMedia, ProductReview, ReviewMedia


class ReviewMediaAdmin(admin.StackedInline):
    model = ReviewMedia
    classes = ["collapse"]
    extra = 0


class ProductReviewInlineAdmin(admin.StackedInline):
    model = ProductReview
    classes = ["collapse"]
    extra = 0


class ProductMediaAdmin(TranslationStackedInline):
    model = ProductMedia
    classes = ['collapse']
    extra = 0


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    inlines = [ProductMediaAdmin, ProductReviewInlineAdmin]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewMediaAdmin]
