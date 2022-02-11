from django.http import JsonResponse
from django.views.generic import View

from feedback.forms import FeedbackForm
from feedback.models import Subscriber


class FeedbackView(View):
    def post(self, request):
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return JsonResponse({"status": 'ok'})
        return JsonResponse({"status": 'error'})


class SubscribeView(View):
    def post(self, request):
        data = request.POST
        try:
            Subscriber.objects.get(email=data.get("email"))
        except Subscriber.DoesNotExist:
            Subscriber.objects.create(email=data.get("email"))
        return JsonResponse({"status": 'ok'})

