# Generated by Django 5.0.1 on 2024-06-07 00:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_photograph_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='date_uploaded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]