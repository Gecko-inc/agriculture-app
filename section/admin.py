from django.contrib import admin
from .models import News, License
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(News)
class ArticleAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(License)
class LicenseAdmin(TabbedTranslationAdmin):
    pass
