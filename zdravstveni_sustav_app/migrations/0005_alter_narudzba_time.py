# Generated by Django 4.1.7 on 2023-09-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zdravstveni_sustav_app', '0004_narudzba_vrijeme_pregelda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narudzba',
            name='time',
            field=models.CharField(choices=[('jutro', 'Jutro'), ('večer', 'Večer')], max_length=10),
        ),
    ]
