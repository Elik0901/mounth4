from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    created_data = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name



