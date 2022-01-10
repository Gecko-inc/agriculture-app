from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Пользователь"), blank=True, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Корзина")
        verbose_name_plural = _("Корзины")

    def __str__(self):
        return _(f"Корзина #{self.id}")

    @property
    def total(self):
        return sum([item.product.price * item.quantity for item in self.cart_item.all()])

    @classmethod
    def get_cart(cls, user):
        try:
            cart = cls.objects.get(user=user)
        except cls.DoesNotExist:
            cart = cls.objects.create(user=user)

        return cart


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_("Корзина"), on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey("catalog.Product", verbose_name="Товар", on_delete=models.CASCADE)
    quantity = models.IntegerField("Количество", default=1)

    class Meta:
        verbose_name = _("Товар в корзине")
        verbose_name_plural = _("Товары в корзине")

    def __str__(self):
        return _(f"Товар #{self.id}")

    @property
    def total(self):
        return self.product.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Пользователь"), blank=True, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField("Имя", max_length=130)
    last_name = models.CharField("Фамилия", max_length=130)
    email = models.CharField("E-Mail", max_length=130)
    phone = models.CharField("Телефон", max_length=130)
    total = models.DecimalField("Итого", max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self):
        return f"Заказ #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Заказ"), on_delete=models.CASCADE, related_name="order_item")
    product = models.ForeignKey("catalog.Product", verbose_name="Товар", on_delete=models.CASCADE)
    quantity = models.IntegerField("Количество", default=1)
    total = models.DecimalField("Итого", max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("Товар в заказе")
        verbose_name_plural = _("Товары в заказе")

    def __str__(self):
        return f"Товар #{self.id}"
