# Generated by Django 2.1.3 on 2019-05-13 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0037_auto_20190513_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 15, 43, 59, 52043), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]
