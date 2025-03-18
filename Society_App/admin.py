

# Register your models here.
from django.contrib import admin
from .models import Farmer, Seedling, Order, Distributor, TrainingProgram

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'location', 'Acres', 'registered_on')
    search_fields = ('name', 'email', 'phone_number', 'location', 'Acres', 'registered_on')
    list_filter = ('location', 'registered_on')
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
