from django.http import JsonResponse
from django.views.generic import DetailView

from catalog.models import Product, ProductReview
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
        ProductReview.objects.create(
            product=self.get_object(),
            user=request.user,
            rate=data.get('rating', 0),
            text=data.get("text", " "),
            is_active=False
        )
        return JsonResponse({"msg": "success"})
