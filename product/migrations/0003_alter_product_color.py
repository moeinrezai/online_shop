# Generated by Django 5.1.4 on 2025-01-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.colors'),
        ),
    ]
