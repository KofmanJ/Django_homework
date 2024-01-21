from django.urls import path

from catalog.views import home, ProductListView, ProductDetailView, ContactView, CategoryListView, \
    ProductCategoryListView, ProductCreateView, ProductUpdateView, ProductDeleteView

from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', home),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('product_list/<int:pk>/', ProductCategoryListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
