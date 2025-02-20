from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class AddTask(models.Model):
    status_types = (
        (1, "Completed"),
        (2, "Pending"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=status_types, default=1)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
