from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product


# Create your views here.


# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
    model = Product


# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('product_name', 'product_description', 'category', 'product_price', 'product_image',)


class ContactView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


# def product(request, pk):
#     context = {
#         'object_list': Product.objects.filter(id=pk)
#     }
#     return render(request, 'catalog/product_detail.html', context)


class ProductDetailView(DetailView):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'object_list': Product.objects.filter(id=pk),
        }
        return render(request, 'catalog/product_detail.html', context)
