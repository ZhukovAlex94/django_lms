# Generated by Django 4.1.1 on 2022-10-15 09:01

import core.validators
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(db_column='first_name_column', max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"first_name" field less than two symbols')], verbose_name='first name')),
                ('last_name', models.CharField(db_column='last_name_column', error_messages={'min_length': '"last_name" field less than two symbols'}, max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='last_name')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('email', models.EmailField(max_length=254, validators=[core.validators.ValidEmailDomain('@gmail.com', '@yahoo.com', '@test.com', '@icloud.com', '@tenet.com'), core.validators.validate_unique_email])),
                ('phone_number', models.CharField(max_length=50, verbose_name='phone_number')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='groups.group')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
