# Generated by Django 3.2.7 on 2021-09-15 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sehat_in_webproject', '0006_auto_20210915_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reportType',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
