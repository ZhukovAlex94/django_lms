from datetime import date

# from faker import Faker

from core.models import BaseModel
from core.validators import validate_start_date

from django.core.validators import MinLengthValidator
from django.db import models

# from courses.models import Course
from teachers.models import Teacher


class Group(BaseModel):
    group_name = models.CharField(
        max_length=100,
        verbose_name='group name',
        db_column='group_name',
        validators=[MinLengthValidator(2, '"group_name" field less than two symbols')]
    )
    group_start_date = models.DateField(default=date.today, null=True, blank=True, validators=[validate_start_date])
    group_description = models.TextField(max_length=1000)
    group_end_date = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    teachers = models.ManyToManyField(
        to=Teacher,
        null=True,
        blank=True,
        related_name='groups'
    )

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f"Group: '{self.group_name}'"

    @classmethod
    def gen_group(cls):
        # f = Faker()
        lst = [
            'Python',
            'Java',
            'PM',
            'DevOps',
            'FrontEnd',
            'QA'
        ]

        for group in lst:
            Group.objects.create(
                group_name=group
            )
