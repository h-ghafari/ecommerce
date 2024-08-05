from django.urls import path
from product.views import (
    CreateCategoryView,
    UpdatedCategoryView,
    DeleteCategoryView,
    CreateProductView,
    UpdateProductView,
    DeleteProductView,
)

urlpatterns = [
    path('category/create/', CreateCategoryView.as_view(), name='create-category'),
    path('category/update/<int:pk>/', UpdatedCategoryView.as_view(), name='update-category'),
    path('category/delete/<int:pk>/', DeleteCategoryView.as_view(), name='delete-category'),
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update-product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),
]