from product.models import Category, Product
from product.serializer import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

class CreateCategoryView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

class UpdatedCategoryView(UpdateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(updated_by=user)

class DeleteCategoryView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()

class CreateProductView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

class UpdateProductView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(updated_by=user)

class DeleteProductView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
