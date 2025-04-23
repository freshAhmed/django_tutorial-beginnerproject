from django.db import models



class Product(models.Model):
  title =models.CharField(max_length=10)
  price =models.DecimalField(decimal_places=3,max_digits=10)
  description=models.TextField(blank=True)
  summary=models.TextField(default='cool!') 