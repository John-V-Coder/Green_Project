

# Register your models here.
from django.contrib import admin
from .models import Farmer, Seedling, Order, Distributor, TrainingProgram

admin.site.register(Farmer)
admin.site.register(Seedling)
admin.site.register(Order)
admin.site.register(Distributor)
admin.site.register(TrainingProgram)
