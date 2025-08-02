from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(default="No description")
    def __str__(self):
        return self.name
