from django.db import models
from core.models import CustomUser


class Teacher(CustomUser):
    MATH = 'math'
    SCIENCE = 'science'
    HISTORY = 'history'
    ENGLISH = 'english'
    ART = 'art'

    SUBJECT_CHOICES = (
        (MATH, 'Mathematics'),
        (SCIENCE, 'Science'),
        (HISTORY, 'History'),
        (ENGLISH, 'English'),
        (ART, 'Art'),
    )
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
