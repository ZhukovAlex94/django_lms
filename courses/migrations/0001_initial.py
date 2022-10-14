# Generated by Django 4.1.1 on 2022-10-12 17:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0004_group_headman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(db_column='course_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"first_name" field less than two symbols')], verbose_name='course_name')),
                ('duration', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('group', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_group', to='groups.group')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]