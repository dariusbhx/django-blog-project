# Generated by Django 3.0.3 on 2020-07-14 00:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200712_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 0, 19, 45, 240455, tzinfo=utc)),
        ),
    ]
