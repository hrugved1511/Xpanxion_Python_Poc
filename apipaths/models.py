from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    price = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    class Meta:
        db_table = "products"
