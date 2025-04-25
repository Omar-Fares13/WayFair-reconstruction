from django.urls import path
from .views import shop_view, product_detail_view,shop_by_category

urlpatterns = [
    path('shop/', shop_view, name='shop'),
    path('product/<int:pk>/', product_detail_view, name='product_detail'),
    path('shop/category/<slug:category_slug>/', shop_by_category, name='shop_by_category'),
]
