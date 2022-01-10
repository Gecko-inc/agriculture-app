from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView, DetailView

from catalog.models import Category, Product
from config.views import common_context
from section.models import News, License


class Index(TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update(common_context())
        categories = Category.objects.filter(is_active=True)
        try:
            category = self.request.GET.get('category', categories[0].id)
            products_list = Product.objects.filter(is_active=True, category_id=category)
            page_num = self.request.GET.get('page', 1)
            paginator = Paginator(products_list, 6)
            try:
                products = paginator.page(page_num)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
            context['products'] = products
            context['products_count'] = len(products_list)
        except IndexError:
            context['products_count'] = 0
        except ValueError:
            context['products_count'] = 0

        return context


class NewsView(TemplateView):
    template_name = "page/news.html"

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context.update(common_context())
        news_list = News.objects.filter(is_active=True)
        page_num = self.request.GET.get('page', 1)
        paginator = Paginator(news_list, 4)
        try:
            news = paginator.page(page_num)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        context['news'] = news
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'page/one-news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context.update(common_context())
        return context


class ContactView(TemplateView):
    template_name = 'page/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context.update(common_context())
        return context


class LicenseView(TemplateView):
    template_name = "page/certificate.html"

    def get_context_data(self, **kwargs):
        context = super(LicenseView, self).get_context_data(**kwargs)
        context.update(common_context())
        context["license"] = License.objects.filter(is_active=True)
        return context


