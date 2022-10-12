# Generated by Django 4.1.1 on 2022-10-12 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_create_datetime_student_group_and_more'),
        ('groups', '0003_group_create_datetime_group_group_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headman',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headman_group', to='students.student'),
        ),
    ]
