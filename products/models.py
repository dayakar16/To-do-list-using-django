from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=None)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    paid = models.BooleanField(default=True)