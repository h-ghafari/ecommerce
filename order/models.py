from django.db import models
from user.models import CustomUser, Address
from product.models import Product

class Order(models.Model):

    class Status(models.TextChoices):
        OPENED = '1', 'Opened'
        PLACED = '2', 'Placed'
        SENT = '3', 'Sent'
        DELIVERD = '4', 'Deliverd'

    class SendTime(models.TextChoices):
        MORNING = '1', '9-12'
        NOON = '2', '12-15'
        AFTERNOON = '3', '15-18'
        NIGHT = '4', '18-21'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order_user')
    status = models.CharField(choices=Status.choices, default=Status.OPENED)
    send_date = models.DateField(null=True, blank=True)
    send_time = models.CharField(choices=SendTime.choices, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, 
                                   on_delete=models.PROTECT, 
                                   null=True, 
                                   blank=True, 
                                   related_name='user_updated_order')
    
    def calculate_order_cost(self):
        cost = float(0)
        items = Item.objects.filter(order=self)
        for item in items:
            cost += (item.product.price * item.count)
            
        return cost

    
class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_product')
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='related_order')

    added_at = models.DateTimeField(auto_now_add=True)

