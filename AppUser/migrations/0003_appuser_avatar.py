# Generated by Django 4.0.4 on 2022-04-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0002_appuser_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='avatar',
            field=models.ImageField(default='avatars/user.png', null=True, upload_to='avatars/'),
        ),
    ]
