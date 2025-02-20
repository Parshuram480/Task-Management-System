from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AddTask(models.Model):
    status_types = (
        (1, "Completed"),
        (2, "Pending"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=status_types, default=1)

    def __str__(self):
        return self.name
