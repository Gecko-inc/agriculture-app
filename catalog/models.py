from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from config.core import get_upload_to


class Category(models.Model):
    IMAGE_PATH = "catalog/category"

    title = models.CharField(_("Название"), max_length=130)
    description = models.TextField(_("Описание"), blank=True)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to)

    is_active = models.BooleanField(_("Статус активности"), default=True)
    sort = models.IntegerField(_('Сортировка'), default=0, help_text=_('Чем ниже число, тем приоритетнее позиция. '
                                                                       'Допустимо использование знака "минус".'))

    class Meta:
        ordering = ['sort', ]
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self) -> str:
        return self.title

    @property
    def product_count(self) -> int:
        return len(self.products.all())


class Product(models.Model):
    IMAGE_PATH = "catalog/product"

    title = models.CharField(_("Название"), max_length=130)
    article = models.CharField(_("Артикул"), max_length=130)
    category = models.ForeignKey(Category, verbose_name=_("Категория"),
                                 related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to)
    description = RichTextUploadingField(_("Описание"), blank=True)
    specifications = RichTextUploadingField(_("Описание"), blank=True)
    info = RichTextUploadingField(_("Описание"), blank=True)
    file = models.FileField(_("Файл"), blank=True, null=True)
    cert = models.FileField(_("Сертификат"), blank=True, null=True)
    iframe = models.TextField(_("Видео с YouTube"), blank=True)
    is_active = models.BooleanField(_("Статус активности"), default=True)

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")

    def __str__(self) -> str:
        return self.title

    @property
    def avg_rate(self) -> int:
        rate_list = [item.rate for item in self.review.filter(is_active=True)]
        avg = int(sum(rate_list)/len(rate_list)) if len(rate_list) != 0 else 0
        return avg

    @property
    def review_count(self) -> int:
        return len(self.review.filter(is_active=True))


class ProductMedia(models.Model):
    IMAGE_PATH = "catalog/media/product"

    product = models.ForeignKey(Product, verbose_name="товар", related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=False)
    sort = models.IntegerField(_('Сортировка'), default=0, help_text=_('Чем ниже число, тем приоритетнее позиция. '
                                                                       'Допустимо использование знака "минус".'))

    class Meta:
        ordering = ['sort', ]
        verbose_name_plural = _("Медиа")
        verbose_name = _("Медиа")

    def __str__(self):
        return f"#{self.id}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, verbose_name="товар", related_name='review', on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=130, null=True)
    email = models.CharField("E-Mail", max_length=130, null=True)
    advantages = models.TextField("Достоинства", null=True)
    disadvantages = models.TextField("Недостатки", null=True)
    text = models.TextField("Текст", null=True)
    rate = models.IntegerField("Оценка", default=0)
    is_active = models.BooleanField(_("Статус активности"), default=True)
    date = models.DateField("Дата", default=timezone.now)

    class Meta:
        ordering = ['-date', '-id']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.name} | {self.date}"


class ReviewMedia(models.Model):
    comment = models.ForeignKey(ProductReview, on_delete=models.CASCADE, verbose_name="Комментарий",
                                related_name='comment_media')
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=False)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"#{self.id}"


