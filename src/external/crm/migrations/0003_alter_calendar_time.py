# Generated by Django 5.1.7 on 2025-04-02 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_task_parenttask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 2, 10, 56, 31, 595537)),
        ),
    ]
