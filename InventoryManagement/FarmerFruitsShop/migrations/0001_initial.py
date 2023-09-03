# Generated by Django 4.2 on 2023-09-02 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.TimeField()),
                ('from_location', models.CharField(max_length=70)),
                ('to_location', models.CharField(max_length=70)),
                ('quantity', models.IntegerField()),
                ('p_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmerFruitsShop.product')),
            ],
        ),
    ]
