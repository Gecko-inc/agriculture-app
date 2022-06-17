from django.http import JsonResponse
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from config.views import common_context
from order.models import Cart, CartItem, Order, OrderItem
import json
from django.shortcuts import redirect


class CartView(TemplateView):
    template_name = 'page/basket.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context.update(common_context())
        context['cart'] = Cart.get_cart(self.request.user)

        return context

    @classmethod
    def add_item(cls, request):
        cart = Cart.get_cart(request.user)
        CartItem.objects.create(
            cart=cart,
            product_id=request.POST.get("product_id"),
            quantity=1,
        )
        return JsonResponse({
            'msg': 'Ok'
        })

    @classmethod
    def delete_item(cls, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cart = Cart.get_cart(request.user)
        try:
            CartItem.objects.get(cart=cart, id=body.get('id')).delete()
        except CartItem.DoesNotExist:
            pass
        cart = Cart.get_cart(request.user)
        return JsonResponse({
            "html": render_to_string("include/cart-item.html", {"cart": cart}), "total": cart.total
        })

    @classmethod
    def edit_item(cls, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cart = Cart.get_cart(request.user)
        try:
            item = CartItem.objects.get(cart=cart, id=body.get('id'))
            if body.get('action') == "-":
                item.quantity -= 1
                item.save()
            else:
                item.quantity += 1
                item.save()
            if item.quantity <= 0:
                item.delete()
        except CartItem.DoesNotExist:
            pass
        cart = Cart.get_cart(request.user)
        return JsonResponse({
            "html": render_to_string("include/cart-item.html", {"cart": cart}), "total": cart.total
        })


class OrderView(TemplateView):
    template_name = "page/regist-order.html"
    
    def get(self, request):
        cart = Cart.get_cart(request.user)
        if cart.total == 0:
            return redirect("/cart")
        return super(OrderView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context.update(common_context())
        context['cart'] = Cart.get_cart(self.request.user)
        return context

    @classmethod
    def confirm_order(cls, request):
        data = request.POST
        cart = Cart.get_cart(request.user)
        order = Order.objects.create(
            user=request.user,
            first_name=data.get("name"),
            last_name=data.get("surname"),
            phone=data.get("phone"),
            email=data.get("email"),
            total=cart.total
        )
        for item in cart.cart_item.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                total=item.total,
                quantity=item.quantity,
            )

        cart.delete()

        return JsonResponse({
            'msg': 'ok'
        })

