# Generated by Django 4.0.1 on 2022-01-20 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_image_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='uuid',
            new_name='unique_id',
        ),
    ]
