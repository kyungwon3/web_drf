from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(modules.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
