# person_api/models.py

from django.db import models
from django.core.validators import RegexValidator


class Person(models.Model):
    name = models.CharField(max_length=255, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z\s]+$',
            message='Name must contain only letters and spaces',
            code='invalid_name'
        )
    ])
    # Add more fields as needed

    def __str__(self):
        return self.name
