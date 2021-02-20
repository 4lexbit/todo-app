from datetime import datetime
from django.contrib.auth.models import User

from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1200)
    creation_date = models.DateField(default=datetime.now)
    completion_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return '%s - %s' % (self.owner.username, str(self.creation_date))

    class Meta():
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
