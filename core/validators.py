# gmail.com, yahoo.com, test.com
from datetime import date

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from students import models


def valid_email_domains(value):
    valid_domains = ['@gmail.com', '@yahoo.com']
    for domain in valid_domains:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email <<{value}>> is incorrect address.')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Invalid email address. The domain <<{args[0].split("@")[1]}>> not valid.')


def validate_unique_email(email):
    if models.Student.objects.filter(email__iexact=email).exists():
        raise ValidationError(f'Entered email: <<{email}>> already existing in the system.')
    return email


def validate_start_date(value):
    if value < date.today():
        raise ValidationError(f'Entered date: {value} is incorrect. Group start date can be equal or later,'
                              f' than today`s date.')
    return value
