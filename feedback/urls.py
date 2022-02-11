from django.urls import path
from .views import FeedbackView, SubscribeView

app_name = "feedback"

urlpatterns = [
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('subs/', SubscribeView.as_view(), name='SubscribeView')
]
