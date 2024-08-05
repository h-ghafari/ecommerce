from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_address')
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    Area_code = models.IntegerField()
    address = models.TextField(max_length=150)
    house_number = models.IntegerField()
    unit = models.IntegerField()
    floor = models.IntegerField()
    zip_code = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(CustomUser,
                                    on_delete=models.PROTECT, 
                                    blank=True, 
                                    null=True, 
                                    related_name='user_modified_address')
