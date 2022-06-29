from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    contents = models.TextField()
    score = models.IntegerField(
        validators=[MinValueValidator(0),
                   MaxValueValidator(5)])
    create_date = models.DateTimeField(auto_now_add=True)