from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return render(request, 'catalog/contacts.html', context={'name': name, 'phone': phone, 'message': message})
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
