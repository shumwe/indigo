# Generated by Django 4.0.5 on 2022-07-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_my_signature_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='secret_code',
            field=models.CharField(blank=True, help_text='added to email to verify sender and limit spam', max_length=20, null=True),
        ),
    ]
