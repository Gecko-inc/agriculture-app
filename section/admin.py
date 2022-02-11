import threading

from django.contrib import admin

from config.models import Config
from feedback.models import Subscriber
from .core import send_mail
from .models import News, License
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(News)
class ArticleAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not obj.id:
            try:
                site_url = Config.objects.get(key="url").value
                text = f"Новая новость {site_url}/news/{obj.slug}/"
                for item in Subscriber.objects.all():
                    threading.Thread(target=send_mail, name="send",
                                     args=(item.email, text, f"Новая новость на сайте {site_url}")).start()
            except Config.DoesNotExist:
                pass
        obj.save()


@admin.register(License)
class LicenseAdmin(TabbedTranslationAdmin):
    pass
