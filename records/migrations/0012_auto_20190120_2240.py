# Generated by Django 2.1.3 on 2019-01-20 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_auto_20190119_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 20, 22, 40, 0, 667343), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]
