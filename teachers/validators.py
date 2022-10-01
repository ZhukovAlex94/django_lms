from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from teachers import models


def valid_email_domains(value):
    valid_domains = ['@gmail.com', '@yahoo.com', '@test.com', '@icloud.com', '@tenet.com']
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
            raise ValidationError(f'Invalid email address. The domain <<{args[0].split("@")[1]} not valid.')


def validate_unique_email(email):
    if models.Teacher.objects.filter(email__iexact=email).exists():
        raise ValidationError(f'Entered email: <<{email}>> already existing in the system.')
    return email
