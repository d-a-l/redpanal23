# Generated by Django 2.2.12 on 2020-05-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_auto_20200510_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='position_lat',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True, verbose_name='latitude'),
        ),
        migrations.AddField(
            model_name='audio',
            name='position_long',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True, verbose_name='longitude'),
        ),
    ]