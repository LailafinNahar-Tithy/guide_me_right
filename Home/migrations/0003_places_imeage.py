# Generated by Django 4.2.7 on 2024-01-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='imeage',
            field=models.ImageField(blank=True, null=True, upload_to='PlaceImeage/'),
        ),
    ]
