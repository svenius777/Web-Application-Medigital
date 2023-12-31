# Generated by Django 4.1.7 on 2023-09-04 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zdravstveni_sustav_app', '0011_doktor_slika_doktora_delete_narudzba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narudzba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_pacijenta', models.CharField(max_length=30)),
                ('prezime_pacijenta', models.CharField(max_length=30)),
                ('telefon_pacijenta', models.CharField(max_length=20)),
                ('email_pacijenta', models.EmailField(max_length=254)),
                ('datum_pregleda', models.DateField(default=django.utils.timezone.now)),
                ('vrijeme_pregleda', models.CharField(choices=[('jutro', 'Jutro'), ('večer', 'Večer')], max_length=10)),
                ('simptomi', models.TextField(blank=True, null=True)),
                ('doktor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
