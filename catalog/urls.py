from django.urls import path

from catalog.views import home, ProductListView, ProductDetailView, ContactView

from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', home),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
]
