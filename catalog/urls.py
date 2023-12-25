from django.urls import path

from catalog.views import index, contacts, home, product

urlpatterns = [
    path('index/', index),
    path('contacts/', contacts),
    path('', home),
    path('product/<int:pk>/', product, name='product')
]
