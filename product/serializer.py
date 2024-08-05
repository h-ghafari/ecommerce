from product.models import Category, Product
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_by']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['category','created_by']

