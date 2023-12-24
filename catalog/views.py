from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return render(request, 'catalog/contacts.html', context={'name': name, 'phone': phone, 'message': message})
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
