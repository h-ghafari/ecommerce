from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from helpers.permissions import IsSelfOrAdmin, IsRelatedOrAdmin
from user.serializers import CustomUserSerializer, SuperUserSerializer, AddressSelializer
from user.models import CustomUser, Address

class CreateUserView(CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()

class CreateSuperUserView(CreateAPIView):
    serializer_class = SuperUserSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()

class CreateAddressView(CreateAPIView):
    serializer_class = AddressSelializer
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class UpdateUserView(UpdateAPIView):
    permission_classes = [IsSelfOrAdmin]
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class UpdateAddressView(UpdateAPIView):
    permission_classes = [IsRelatedOrAdmin]
    serializer_class = AddressSelializer
    queryset = Address.objects.all()

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class DeleteUserView(DestroyAPIView):
    permission_classes = [IsSelfOrAdmin]
    queryset = CustomUser.objects.all()

class DeleteAddressView(DestroyAPIView):
    permission_classes = [IsRelatedOrAdmin]
    queryset = Address.objects.all()



