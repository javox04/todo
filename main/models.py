from django.db import models

class Todo(models.Model):
    tack = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="In Progress")


    def __str__(self):
        return  self.task
