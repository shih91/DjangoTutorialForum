# Generated by Django 3.2.8 on 2021-10-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20211025_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', upload_to=''),
        ),
    ]
