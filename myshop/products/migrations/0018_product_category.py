# Generated by Django 5.0.2 on 2024-03-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='products.category'),
        ),
    ]
