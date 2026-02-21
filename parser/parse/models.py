from django.db import models
from django.template.defaultfilters import slugify

class ReqSite(models.Model):

    class Site(models.TextChoices):
        NEW = 'new', 'Новый'
        PROCESSING = 'processing', 'В процессе'
        DONE = 'done', 'Завершен'
        ERROR = 'error', 'Ошибка'
        


    name = models.CharField(max_length=31)
    slug = models.SlugField(null=True, default=None)
    url = models.URLField()

    status = models.CharField(
        max_length=15,
        default=Site.NEW,
        choices=Site.choices,
    )

    time_request = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"Сайт - {self.name}, URL - {self.url}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
class ParsedData(models.Model):
    site = models.ForeignKey(ReqSite, on_delete=models.CASCADE, related_name='parsed_data')
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    time_response = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Данные для сайта - {self.site.name}"
    
    @property
    def duration_time(self):
        if self.site.time_request and self.time_response:
            return str(self.time_response - self.site.time_request)
        return None