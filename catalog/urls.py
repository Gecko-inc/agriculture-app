from django.urls import path
from .views import ProductView

app_name = "section"

urlpatterns = [
    path('product/<int:pk>/', ProductView.as_view(), name='product')
]
