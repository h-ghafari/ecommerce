from django.db import models
from user.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='user_created_category')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser,
                                   on_delete=models.PROTECT, 
                                   null=True, 
                                   blank=True, 
                                   related_name='user_updated_category')


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category')
    description = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='user_created_product')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, 
                                   on_delete=models.PROTECT, 
                                   null=True, 
                                   blank=True, 
                                   related_name='user_updated_product')