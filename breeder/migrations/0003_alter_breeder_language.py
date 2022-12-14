# Generated by Django 4.1.1 on 2022-09-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeder', '0002_alter_breeder_address_alter_breeder_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breeder',
            name='language',
            field=models.CharField(choices=[('en-us', 'English'), ('ro', 'Romanian'), ('fr', 'French'), ('nl', 'Dutch'), ('de', 'German'), ('it', 'Italian'), ('es', 'Spanish')], default='en-us', max_length=5, verbose_name='language'),
        ),
    ]
