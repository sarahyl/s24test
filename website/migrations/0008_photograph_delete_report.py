# Generated by Django 5.0.1 on 2024-06-06 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_adminuser_regularuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255)),
                ('image_type', models.CharField(max_length=255, null=True)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
