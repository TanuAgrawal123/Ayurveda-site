# Generated by Django 2.0.13 on 2019-03-30 05:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ayurvedasite', '0004_auto_20190330_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 5, 44, 11, 342497, tzinfo=utc)),
        ),
    ]
