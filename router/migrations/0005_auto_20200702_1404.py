# Generated by Django 3.0.8 on 2020-07-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0004_auto_20200702_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='loopback',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]