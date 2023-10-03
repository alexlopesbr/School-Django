import uuid

from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.db import models


class CustomUser(AbstractUser):
    STAFF = 'staff'
    TEATCHER = 'teatcher'
    STUDENT = 'student'

    ROLE_CHOICES = (
        (STAFF, 'staff'),
        (TEATCHER, 'teatcher'),
        (STUDENT, 'student'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=8, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class SchoolClass(models.Model):
    YEAR_CHOICES = [(str(year), f'Year {year}') for year in range(1, 13)]

    year_number = models.CharField(max_length=15, choices=YEAR_CHOICES)
    year_name = models.CharField(max_length=30)

    def __str__(self):
        return self.year_name


class SchoolClassUser(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
