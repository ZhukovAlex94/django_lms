from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        verbose_name='group name',
        db_column='group_name',
        validators=[MinLengthValidator(2, '"group_name" field less than two symbols')]
    )

    group_start_date = models.DateField(default=date.today, null=True, blank=True)

    group_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.group_name
