from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=255)
    priority = models.IntegerField()
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.task
