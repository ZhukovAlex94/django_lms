from django.core.validators import MinLengthValidator
from django.db import models


class Course(models.Model):
    course_name = models.CharField(
        max_length=100,
        verbose_name='course_name',
        db_column='course_name',
        validators=[MinLengthValidator(2, '"first_name" field less than two symbols')]
    )
    duration = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    group = models.OneToOneField(
        'groups.Group',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='course_group'
    )

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f"{self.course_name}"
