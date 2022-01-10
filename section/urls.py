from django.urls import path
from .views import Index, NewsView, NewsDetailView, ContactView, LicenseView

app_name = "section"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('license/', LicenseView.as_view(), name='license'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
]
