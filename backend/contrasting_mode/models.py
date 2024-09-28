from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class ContrastPair(models.Model):
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item1} vs {self.item2}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    pairs = models.ManyToManyField(ContrastPair, related_name='tags')

    def __str__(self):
        return self.name
