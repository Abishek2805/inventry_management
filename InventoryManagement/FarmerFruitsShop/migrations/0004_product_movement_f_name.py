# Generated by Django 4.2 on 2023-09-02 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarmerFruitsShop', '0003_remove_product_movement_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_movement',
            name='f_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_location', to='FarmerFruitsShop.product'),
        ),
    ]
