from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from core.validators import ValidEmailDomain, validate_unique_email


class BaseModel(models.Model):
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com', '@icloud.com', '@tenet.com')

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
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST), validate_unique_email])
    phone_number = models.CharField(
        max_length=50,
        verbose_name='phone_number'
    )

    class Meta:
        abstract = True

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        f = Faker()

        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-15y'),
            email=f'{first_name}.{last_name}{f.random.choice(cls.VALID_DOMAIN_LIST)}',
            phone_number=f.phone_number()
        )
        obj.save()
        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()
