from helpers.permissions import IsRelatedOrAdmin, IsSelfOrAdmin
from user_profile.models import Profile
from user_profile.serializer import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
)

class CreateprofileView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateProfileView(UpdateAPIView):
    permission_classes = [IsRelatedOrAdmin]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
