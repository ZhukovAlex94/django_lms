from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from core.validators import ValidEmailDomain, validate_unique_email

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        db_column='first_name_column',
        validators=[MinLengthValidator(2, '"first_name" field less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last_name',
        db_column='last_name_column',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"last_name" field less than two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)

    # gmail.com, yahoo.com, test.com
    # email = models.EmailField(validators=[valid_email_domains])
    # email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)])
    # email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)], unique=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST), validate_unique_email])

    phone_number = models.CharField(
        max_length=50,
        verbose_name='phone_number'
    )

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'students'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email)
            try:
                st.full_clean()
                st.save()
            except ValidationError:
                print('Incorrect data')
