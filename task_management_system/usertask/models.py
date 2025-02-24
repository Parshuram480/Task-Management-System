from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class AddTask(BaseModel):
    status_types = (
        (1, "Pending"),
        (2, "Completed"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=status_types, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
