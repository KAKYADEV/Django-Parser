from django.db import models

class ReqSite(models.Model):
    name = models.CharField(max_length=31)
    url = models.URLField()
    time_request = models.DateTimeField(auto_now_add=True)
    time_response = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Сайт - {self.name}, URL - {self.url}"