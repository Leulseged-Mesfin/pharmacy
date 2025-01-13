from django.urls import path
from .views import (
    ProductListCreateAPIView, 
    ProductRetrieveUpdateDeleteAPIView,

    SupplierListCreateAPIView,
    SupplierRetrieveUpdateDeleteAPIView,

    OrderListCreateAPIView,
    OrderRetrieveUpdateDeleteAPIView,

    OrderItemListCreateAPIView,
    OrderItemRetrieveUpdateDeleteAPIView,

    PatientListCreateAPIView,
    PatientRetrieveUpdateDeleteAPIView,

    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDeleteAPIView
  
)

urlpatterns = [
    path('products', ProductListCreateAPIView.as_view(), name='products-list'),
    path('products/<pk>', ProductRetrieveUpdateDeleteAPIView.as_view(), name='products-retrieve'),

    path('suppliers', SupplierListCreateAPIView.as_view(), name='suppliers-list'),
    path('suppliers/<pk>', SupplierRetrieveUpdateDeleteAPIView.as_view(), name='suppliers-retrieve'),

    path('orders', OrderListCreateAPIView.as_view(), name='orders-list'),
    path('orders/<pk>', OrderRetrieveUpdateDeleteAPIView.as_view(), name='orders-retrieve'),

    path('orderitems', OrderItemListCreateAPIView.as_view(), name='orders-items-list'),
    path('orderitems/<pk>', OrderItemRetrieveUpdateDeleteAPIView.as_view(), name='orders-items-retrieve'),

    path('patients', PatientListCreateAPIView.as_view(), name='patients-list'),
    path('patients/<pk>', PatientRetrieveUpdateDeleteAPIView.as_view(), name='patients-retrieve'),

    path('category', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('category/<pk>', CategoryRetrieveUpdateDeleteAPIView.as_view(), name='category-retrieve')
]
