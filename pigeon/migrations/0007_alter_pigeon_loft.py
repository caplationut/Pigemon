# Generated by Django 4.1.1 on 2022-09-26 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loft', '0002_alter_loft_address_alter_loft_breeder_and_more'),
        ('pigeon', '0006_alter_pigeon_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigeon',
            name='loft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pigeons', to='loft.loft', verbose_name='loft'),
        ),
    ]
