from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from .models import Category, Product, Image


# Create your views here.
class CategoryView(View):
    template_name = 'rizefir/index.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        products = Product.objects.all()
        images = Image.objects.all()
        return render(request, self.template_name, {'products': products, 'category': category})

    # def post(self, request, *args, **kwargs):
    #     form = ['Зефирные букеты', 'Выпечка', 'Шоколад']
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')-
