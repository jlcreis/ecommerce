# Generated by Django 3.1.3 on 2021-03-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_sale_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
