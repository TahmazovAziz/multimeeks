# Generated by Django 5.0.1 on 2024-01-04 21:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(null=True, upload_to='deploy/videos/%Y/%m/%d/', verbose_name='')),
                ('length', models.DurationField()),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/%y', validators=[django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
        migrations.CreateModel(
            name='FilmView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/')),
                ('length', models.DurationField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
        ),
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(null=True, upload_to='deploy/videos/%Y/%m/%d/', verbose_name='')),
                ('name', models.CharField(max_length=200)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.episods')),
            ],
        ),
    ]
