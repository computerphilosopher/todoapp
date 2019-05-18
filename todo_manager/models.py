from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField(blank=True, null=True)

    priority_error = "우선순위는 1부터 5까지만 지정할 수 있습니다."
    priority = models.IntegerField(default=5, validators=[MaxValueValidator(5, priority_error), MinValueValidator(1, priority_error)])

    finished = models.BooleanField(default=False)
