from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name