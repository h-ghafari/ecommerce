from django.urls import path
from order.views import (
    CreateOrderView,
    UpdateOrderView,
    DeleteOrderView,
    AddItemView,
    DeleteItemView,
)

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('update/<int:pk>/', UpdateOrderView.as_view(), name='update-order'),
    path('delete/<int:pk>/', DeleteOrderView.as_view(), name='delete-order'),
    path('item/add/', AddItemView.as_view(), name='add-item-to-order'),
    path('item/delete/<int:pk>/', DeleteItemView.as_view(), name='delet-item'),
]