from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to Django's User model
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=255)
    acres = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Added farm_size with default
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def email(self):
        """ Get email from linked User model """
        return self.user.email if self.user else "No Email"


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
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=255)

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
    
class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)  
    DONOR_TYPE_CHOICES = [
        ('Individual', 'Individual'),
        ('Organization', 'Organization')
    ]
    donor_type = models.CharField(max_length=20, choices=DONOR_TYPE_CHOICES, default='Individual')
    donor_name = models.CharField(max_length=255, help_text="Enter your full name if Individual, or Organization name if Organization.")
    DONATION_TYPE_CHOICES = [
        ('Money', 'Money (KES)'),
        ('Seedlings', 'Seedlings (Number of Trees)'),
        ('Training', 'Training Sessions')
    ]
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="If 'Money', enter amount in KES. If 'Seedlings', enter number of trees.")
    PAYMENT_OPTIONS = [
        ('Mpesa', 'Mpesa'),
        ('Bank Transfer', 'Bank Transfer'),
        ('PayPal', 'PayPal'),
        ('Credit/Debit Card', 'Credit/Debit Card'),
        ('Cash', 'Cash')
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_OPTIONS, blank=True, null=True, help_text="Only required if donating money.")

    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

    def clean(self, *args, **kwargs):
        """ Ensure payment method is required only for monetary donations """
        if self.donation_type == 'Money' and not self.payment_method:
            raise ValueError("Payment method is required for monetary donations.")
        super().save(*args, **kwargs)

    def __str__(self):
        donation_detail = f"{self.amount} KES" if self.donation_type == "Money" else f"{self.amount} Trees"
        return f"{self.donor_name} ({self.donor_type}) - {self.donation_type} - {donation_detail}"