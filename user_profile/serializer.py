from rest_framework.serializers import ModelSerializer
from user_profile.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile
        exclude=['user']
