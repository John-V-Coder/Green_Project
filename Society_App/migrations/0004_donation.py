# Generated by Django 5.1.7 on 2025-03-19 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0003_rename_farm_size_farmer_acres_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_type', models.CharField(choices=[('Individual', 'Individual'), ('Organization', 'Organization')], default='Individual', max_length=20)),
                ('donor_name', models.CharField(help_text='Enter your full name if Individual, or Organization name if Organization.', max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('donation_type', models.CharField(choices=[('Money', 'Money'), ('Seedlings', 'Seedlings'), ('Training', 'Training')], max_length=20)),
                ('payment_method', models.CharField(choices=[('Mpesa', 'Mpesa'), ('Bank Transfer', 'Bank Transfer'), ('PayPal', 'PayPal'), ('Credit/Debit Card', 'Credit/Debit Card'), ('Cash', 'Cash')], default='Mpesa', max_length=20)),
                ('message', models.TextField(blank=True, null=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
