from .models import News, License
from modeltranslation.translator import translator, TranslationOptions


class NewsTrans(TranslationOptions):
    fields = [
        'title',
        'image',
        'text',
    ]


class LicenseTrans(TranslationOptions):
    fields = [
        'title',
        'image',
    ]


translator.register(License, LicenseTrans)
translator.register(News, NewsTrans)
