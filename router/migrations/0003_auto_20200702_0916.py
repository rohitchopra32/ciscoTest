# Generated by Django 3.0.8 on 2020-07-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0002_auto_20200702_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='router_type',
            field=models.CharField(choices=[('0', 'Select Router Type'), ('AG1', 'AG1'), ('CSS', 'CSS')], default='0', max_length=3),
        ),
    ]