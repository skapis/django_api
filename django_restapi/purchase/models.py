import uuid
from django.contrib.auth.models import User
from django.db import models


class Purchase(models.Model):
    purchase_id = models.UUIDField(default=uuid.uuid4)
    product = models.CharField(max_length=255)
    amount = models.IntegerField()
    currency = models.CharField(max_length=255)
    unit_price = models.IntegerField()
    total_price = models.IntegerField()
    purchase_date = models.DateField()
    payment_method = models.CharField(max_length=255, default='Cash')
    shipping_method = models.CharField(max_length=255, default='In the store')
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    street_number = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, related_name='purchases')

    def __str__(self):
        return self.product



