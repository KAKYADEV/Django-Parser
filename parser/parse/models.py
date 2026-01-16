from django.db import models

class ReqSite(models.Model):
    name = models.CharField(max_length=31)
    url = models.URLField()
    time_request = models.TimeField(auto_now_add=True)
    time_response = models.TimeField()
    duration = models.DurationField()
    active = models.BooleanField()