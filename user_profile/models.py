from django.db import models
from user.models import CustomUser, Address

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profile_related_user')
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=200)
    active_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='active_address')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    updated_by = models.ForeignKey(CustomUser, 
                                   on_delete=models.PROTECT, 
                                   null=True, 
                                   blank=True, 
                                   related_name='user_updated_profile')