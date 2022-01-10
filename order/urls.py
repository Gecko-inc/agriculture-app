from django.urls import path
from .views import CartView, OrderView
from django.views.decorators.csrf import csrf_exempt

app_name = "section"

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('order/confirm/', OrderView.confirm_order, name='confirm_order'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', CartView.add_item, name='add_item'),
    path('cart/delete/', csrf_exempt(CartView.delete_item), name='delete_item'),
    path('cart/edit/', csrf_exempt(CartView.edit_item), name='edit_item'),
]
