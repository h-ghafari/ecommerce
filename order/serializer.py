from rest_framework.serializers import ModelSerializer
from order.models import Order, Item

class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        exclude=['user']

class ItemSerializer(ModelSerializer):
    class Meta:
        model=Item
