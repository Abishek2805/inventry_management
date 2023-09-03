# Generated by Django 4.2 on 2023-09-02 14:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FarmerFruitsShop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_movement',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product_movement',
            name='from_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_location', to='FarmerFruitsShop.location'),
        ),
        migrations.AlterField(
            model_name='product_movement',
            name='to_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_location', to='FarmerFruitsShop.location'),
        ),
    ]
