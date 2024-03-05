from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
