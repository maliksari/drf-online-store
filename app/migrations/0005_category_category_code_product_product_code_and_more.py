# Generated by Django 4.1.9 on 2023-06-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_description_alter_cart_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_code',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]