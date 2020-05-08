from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=30, default="[NONE]")
    last_name = models.CharField(max_length=30, default="[NONE]")
    favorite_food = models.CharField(max_length=30, default="[NONE]")
    order_time = timezone.now()
    def __str__(self):
        return self.first_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ENTREE_CHOICES = (
        ('NA', 'NONE'),
        ('HAM', 'Hamburger'),
        ('CHZ', 'Cheeseburger'),
        ('TAC', 'Taco'),
        ('FSH', 'Fish Sandwich')
    )
    SIDE_CHOICES = (
        ('NA', 'NONE'),
        ('FRI', 'Fries'),
        ('BNS', 'Beans'),
        ('SAL', 'Salad'),
        ('ORG', 'Organs')
    )
    entree = models.CharField(max_length=30, choices=ENTREE_CHOICES, default="NA")
    side = models.CharField(max_length=30, choices=SIDE_CHOICES, default="NA")
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.entree









