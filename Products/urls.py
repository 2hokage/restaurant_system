from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show-products', views.products, name='products'),
    path('product/<int:productId>', views.product, name="product")
]
