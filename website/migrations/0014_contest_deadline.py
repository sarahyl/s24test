# Generated by Django 5.0.1 on 2024-06-12 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_rename_name_contest_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]