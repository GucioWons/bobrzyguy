# Generated by Django 4.0.3 on 2022-04-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='type',
            field=models.CharField(choices=[('CUSTOMER', 'Customer'), ('WORKER', 'Worker')], default='Worker', max_length=50),
            preserve_default=False,
        ),
    ]