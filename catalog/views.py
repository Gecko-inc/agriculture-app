from django.http import JsonResponse
from django.views.generic import DetailView
from django.core.files import File
from catalog.models import Product, ProductReview, ReviewMedia
from config.views import common_context


class ProductView(DetailView):
    model = Product
    template_name = 'page/Product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context.update(common_context())
        context['comments'] = self.object.review.filter(is_active=True)

        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        image_list = request.FILES.getlist('file')
        comment = ProductReview.objects.create(
            product=self.get_object(),
            name=data.get('name', " "),
            email=data.get('rating', " "),
            rate=data.get('rating', 0),
            advantages=data.get('advantages', " "),
            disadvantages=data.get('disadvantages', " "),
            text=data.get("text", " "),
            is_active=False
        )
        if image_list:
            for item in image_list:
                media = ReviewMedia()
                media.image = File(item, name=str(item))
                media.comment = comment
                media.save()
        return JsonResponse({"msg": "success"})
