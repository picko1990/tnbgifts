# Generated by Django 4.0.1 on 2022-01-20 09:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=100),
        ),
    ]