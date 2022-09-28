# Generated by Django 4.1.1 on 2022-09-26 10:57

import datetime
from django.db import migrations, models
import groups.validators


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, validators=[groups.validators.validate_start_date]),
        ),
    ]
