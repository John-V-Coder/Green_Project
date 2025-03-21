# Generated by Django 5.1.7 on 2025-03-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Society_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='farm_size',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
