# Generated by Django 2.1.3 on 2019-03-13 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0020_auto_20190312_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_students',
            name='Proimage',
        ),
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 7, 32, 24, 591608), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]
