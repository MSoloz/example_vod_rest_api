# Generated by Django 4.2.3 on 2023-08-19 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image_file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
