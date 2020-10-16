from django.db import models
import datetime, pytz

class Task(models.Model):
  task_text = models.CharField(max_length=200)
  creation_date = models.DateTimeField('date created')
  due_date = models.DateTimeField('date[when] due')
  importance = models.CharField(max_length=20)

  def __str__(self):
    return self.task_text

  def is_due(self):
    d = datetime.datetime.now()
    timezone = pytz.timezone("Africa/Lagos")
    d_aware = timezone.localize(d)
    return self.due_date <= d_aware