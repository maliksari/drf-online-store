# Generated by Django 4.1.9 on 2023-06-07 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cart_options_alter_cartitem_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_by',
            field=models.ForeignKey(editable=False, help_text='Oluşturan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_cby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart',
            name='modified_by',
            field=models.ForeignKey(editable=False, help_text='Güncelleyen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_mby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='created_by',
            field=models.ForeignKey(editable=False, help_text='Oluşturan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_cby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='modified_by',
            field=models.ForeignKey(editable=False, help_text='Güncelleyen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_mby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(editable=False, help_text='Oluşturan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_cby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified_by',
            field=models.ForeignKey(editable=False, help_text='Güncelleyen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_mby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(editable=False, help_text='Oluşturan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_cby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='modified_by',
            field=models.ForeignKey(editable=False, help_text='Güncelleyen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_mby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(editable=False, help_text='Oluşturan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_cby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_by',
            field=models.ForeignKey(editable=False, help_text='Güncelleyen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_mby', to=settings.AUTH_USER_MODEL),
        ),
    ]