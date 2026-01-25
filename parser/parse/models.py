from django.db import models

class ReqSite(models.Model):

    class Site(models.TextChoices):
        NEW = 'new', 'Новый'
        PROCESSING = 'processing', 'В процессе'
        DONE = 'done', 'Завершен'
        ERROR = 'error', 'Ошибка'
        


    name = models.CharField(max_length=31)
    url = models.URLField()

    status = models.CharField(
        max_length=15,
        default=Site.NEW,
        choices=Site.choices,
    )

    time_request = models.DateTimeField(auto_now_add=True)
    time_response = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Сайт - {self.name}, URL - {self.url}"