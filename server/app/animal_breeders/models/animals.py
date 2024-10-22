from django.db import models
from .users import User

class Animal(models.Model):
    BREED_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
    ]

    owner = models.ForeignKey(User, related_name='animals', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=50, choices=BREED_CHOICES)

    def __str__(self):
        return f"{self.breed} ({self.age} years old)"