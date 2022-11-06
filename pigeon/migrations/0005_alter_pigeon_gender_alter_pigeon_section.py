# Generated by Django 4.1.1 on 2022-09-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeon', '0004_alter_pigeon_gender_alter_pigeon_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigeon',
            name='gender',
            field=models.CharField(choices=[(None, 'Select section'), ('MA', 'Male'), ('FE', 'Female'), ('NN', 'Unknown')], max_length=32, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='pigeon',
            name='section',
            field=models.CharField(choices=[(None, 'Select section'), ('NE', 'New_entry'), ('YB', 'Young_bird'), ('OB', 'Old_bird'), ('BR', 'Breeding'), ('WH', 'Widow_hen'), ('WC', 'Widow_cock'), ('QT', 'Quarantine')], max_length=32, verbose_name='section'),
        ),
    ]
