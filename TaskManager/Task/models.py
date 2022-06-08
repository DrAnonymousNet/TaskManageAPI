from django.db import models
from .choice import WORK_FLOW


class Task(models.Model):
    title = models.CharField(max_length=50)
    state = models.CharField(max_length= 100, choices=WORK_FLOW, default="draft")

    def __str__(self) -> str:
        return self.title