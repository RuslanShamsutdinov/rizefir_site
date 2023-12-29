from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from .products.models import Product, Category


class AboutView(TemplateView):
    template_name = 'rizefir/about.html'


class IndexView(View):
    template_name = 'rizefir/index.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products, 'category': category})

    # def post(self, request, *args, **kwargs):
    #     form = ['Зефирные букеты', 'Выпечка', 'Шоколад']
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
