from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.utils.text import slugify


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    featured_image = models.ImageField(upload_to="blogs/featured/", blank=True)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # for seo
    meta_description = models.CharField(max_length=200, blank=True)
    meta_keywords = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(BlogPost, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blogs/", blank=True)
