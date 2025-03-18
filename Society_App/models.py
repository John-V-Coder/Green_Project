from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to Django's User model
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=255)
    Acres = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Added farm_size with default
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Seedling(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()
    supplier = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.species}"


class Order(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    seedling = models.ForeignKey(Seedling, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    ordered_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.seedling.price  # Auto-calculate total price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.farmer.name} ({self.status})"


class Distributor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    duration = models.CharField(max_length=60)
    location = models.CharField(max_length=255)
    trainer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
