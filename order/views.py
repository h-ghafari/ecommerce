from order.models import Order, Item
from order.serializer import OrderSerializer, ItemSerializer
from helpers.permissions import IsRelatedOrAdmin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import (
    CreateAPIView, 
    UpdateAPIView, 
    DestroyAPIView,
)

class CreateOrderView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateOrderView(UpdateAPIView):
    permission_classes = [IsRelatedOrAdmin]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class DeleteOrderView(DestroyAPIView):
    permission_classes = [IsRelatedOrAdmin]
    queryset = Order.objects.all()

class AddItemView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def perform_create(self, serializer):
        if serializer.order.user != self.request.user:
            return Response({'error':'user does not match with order'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

class DeleteItemView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()

    def perform_destroy(self, instance):
        if self.request.user.is_staff:
            instance.delete()
        if instance.order.user != self.request.user:
            return Response({'error':'user does not match with order'}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()