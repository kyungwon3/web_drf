from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Review(models.Model):
    score = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)]
    )
    contents = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)