# Generated by Django 4.0 on 2022-01-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_address_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Email',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='Address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
