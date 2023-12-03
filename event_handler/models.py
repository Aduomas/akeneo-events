from django.db import models


class EventLog(models.Model):
    action = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    author_type = models.CharField(max_length=100)
    event_id = models.CharField(max_length=100, unique=True)
    event_datetime = models.DateTimeField()
    pim_source = models.URLField()
    data = models.JSONField()

    def __str__(self):
        return f"{self.action} by {self.author} on {self.event_datetime}"
