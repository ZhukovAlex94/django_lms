from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(value):
    if value < date.today():
        raise ValidationError(f'Entered date: {value} is incorrect. Group start date can be equal or later,'
                              f' than today`s date.')
    return value
