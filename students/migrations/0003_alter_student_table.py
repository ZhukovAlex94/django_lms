# Generated by Django 4.1.1 on 2022-09-21 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_email_alter_student_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='student_table',
        ),
    ]