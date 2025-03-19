

# Register your models here.
from django.contrib import admin
from .models import Farmer, Seedling, Order, Distributor, TrainingProgram, Donation

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'location', 'acres', 'registered_on')
    search_fields = ('name', 'email', 'phone_number', 'location', 'Acres', 'registered_on')
    list_filter = ('location', 'registered_on')

    
    def email(self, obj):
        return obj.user.email  # Fetch email from User model
    email.admin_order_field = 'user__email'  # Allow sorting by email
    email.short_description = 'Email'  # Rename column in admin panel

@admin.register(Seedling)
class SeedlingAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'price', 'quantity_available', 'supplier', 'added_on')
    search_fields = ('name', 'species', 'price', 'quantity_available', 'supplier', 'added_on')
    list_filter = ('species', 'price', 'quantity_available', 'supplier', 'added_on')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'seedling', 'quantity', 'total_price', 'status', 'ordered_on')
    search_fields = ('farmer', 'seedling', 'quantity', 'total_price', 'status', 'ordered_on')
    list_filter = ('status', 'ordered_on')
@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'region')
    search_fields = ('name', 'phone_number', 'email', 'region')
    list_filter = ('region',)
@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time', 'location', 'duration', 'trainer')
    search_fields = ('title', 'description', 'date', 'time', 'location', 'duration', 'trainer')
    list_filter = ('date', 'location', 'duration', 'trainer')
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'donor_type', 'donor', 'donation_type', 'amount', 'payment_method', 'date')  
    search_fields = ('donor_name', 'donor__username', 'donation_type', 'payment_method')
    list_filter = ('donor_type', 'donation_type', 'payment_method', 'date')  
    ordering = ('-date',) 
    
    def save_model(self, request, obj, form, change):
        """ Ensure payment method is required for monetary donations """
        if obj.donation_type == 'Money' and not obj.payment_method:
            raise ValueError("Payment method is required for monetary donations.")
        super().save_model(request, obj, form, change)
    