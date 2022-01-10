from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from config.core import get_upload_to


class News(models.Model):
    IMAGE_PATH = "sections/article"

    title = models.CharField(_("Заголовок"), max_length=130)
    slug = models.CharField(_("URL адрес"), max_length=130, help_text=_("Заполняется автоматически"))
    short_description = models.TextField(_("Краткое описание"), max_length=500, blank=True)
    text = RichTextUploadingField(_('Текст публикации'), blank=True)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=True)
    date = models.DateField("Дата", default=timezone.now)
    is_active = models.BooleanField(_("Активна"), default=False)

    class Meta:
        ordering = ['-date', "-id"]
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")

    def __str__(self):
        return self.title


class License(models.Model):
    IMAGE_PATH = "sections/article"

    title = models.CharField(_("Заголовок"), max_length=130)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=False)
    sort = models.IntegerField(_('Сортировка'), default=0, help_text=_('Чем ниже число, тем приоритетнее позиция. '
                                                                       'Допустимо использование знака "минус".'))
    is_active = models.BooleanField(_("Активна"), default=False)

    class Meta:
        ordering = ['sort']
        verbose_name = "Лицензию"
        verbose_name_plural = "Лицензии"

    def __str__(self):
        return self.title
