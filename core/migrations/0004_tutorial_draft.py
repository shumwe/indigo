# Generated by Django 4.0.5 on 2022-07-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_tutorial_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
