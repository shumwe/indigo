# Generated by Django 4.0.5 on 2022-07-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='featured_image',
            field=models.ImageField(default='featured_images/features.jpg', upload_to='featured_images/'),
        ),
    ]
