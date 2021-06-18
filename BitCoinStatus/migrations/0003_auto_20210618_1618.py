# Generated by Django 3.2.4 on 2021-06-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BitCoinStatus', '0002_auto_20210618_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitcoindata',
            name='truncate_hour_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='bitcoindata',
            name='truncate_minute_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='bitcoindata',
            name='truncate_second_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bitcoindata',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
