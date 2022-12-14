# Generated by Django 4.1.1 on 2022-09-20 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loft',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='loft',
            name='breeder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lofts', to=settings.AUTH_USER_MODEL, verbose_name='breeder'),
        ),
        migrations.AlterField(
            model_name='loft',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='loft',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='loft',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
    ]
