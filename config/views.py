from catalog.models import Category
from .models import Config


def common_context() -> dict:
    """
      Returns the context that is present on all pages
    """
    context = dict()
    context['cfg'] = Config.get_cfg()
    categories = Category.objects.filter(is_active=True)
    context['categories'] = categories
    return context
