from django.db import models

# Create your models here.

class Product(models.Model):
    title= models.CharField(max_length=120)# char fields are always required by default
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=8)
    summary = models.TextField(blank=True,null=True)
    featured =models.BooleanField(default=False)

    def __str__(self):
        return self.title
