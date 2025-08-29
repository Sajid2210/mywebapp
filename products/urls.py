from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    path('shop/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:product_slug>/<slug:variation_slug>/', views.product_detail, name='product_detail_variation'),
]
