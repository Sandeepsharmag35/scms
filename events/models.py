from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class NoticeImage(models.Model):
    notice = models.ForeignKey(Notice, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to="notices/", blank=True)


class Event(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = HTMLField()
    start_date = models.DateField(blank=True)
    start_time = models.TimeField()
    location = models.CharField(max_length=100, blank=True)
    location_iframe_code = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/", blank=True)
