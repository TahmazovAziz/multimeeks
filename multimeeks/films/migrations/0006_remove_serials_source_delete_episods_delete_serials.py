# Generated by Django 5.0.1 on 2024-01-05 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_remove_episods_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serials',
            name='source',
        ),
        migrations.DeleteModel(
            name='Episods',
        ),
        migrations.DeleteModel(
            name='Serials',
        ),
    ]
