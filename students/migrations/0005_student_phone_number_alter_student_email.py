# Generated by Django 4.1.1 on 2022-09-26 10:57

from django.db import migrations, models
import core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_email_alter_student_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=0, max_length=50, verbose_name='phone_number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, validators=[core.validators.ValidEmailDomain('@gmail.com', '@yahoo.com', '@test.com'), core.validators.validate_unique_email]),
        ),
    ]
