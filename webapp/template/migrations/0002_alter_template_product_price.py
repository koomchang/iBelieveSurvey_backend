# Generated by Django 4.1.6 on 2023-05-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='product_price',
            field=models.IntegerField(verbose_name='상품 가격'),
        ),
    ]
