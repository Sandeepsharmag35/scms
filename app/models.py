from django.db import models
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField
from django.utils.text import slugify


# image_Validator
def logoImageValidator(instance, filename):
    ext = filename.split(".")[-1].lower()
    allowed_extensions = ["jpg", "jpeg", "png", "*"]

    if ext in allowed_extensions:
        return f"info/{filename}"
    else:
        raise ValidationError(
            "Invalid file format. Only JPG, JPEG, and PNG files are allowed."
        )


# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=30, default="School/College")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=100, default="School/College Address")
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    logo = models.ImageField(upload_to=logoImageValidator, blank=True)
    featured_image = models.ImageField(upload_to=logoImageValidator, blank=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    description = HTMLField()


class AboutUsImage(models.Model):
    about = models.ForeignKey(AboutUs, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="about/")


class Team(models.Model):
    POST_CHOICES = [
        ("Principal", "Principal"),
        ("Chairman", "Chairman"),
        ("BOD", "BOD"),
        ("Accountant", "Accountant"),
        ("Teacher", "Teacher"),
        ("Staff", "Staff"),
    ]
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=25, choices=POST_CHOICES, default="select")
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
    )
    facebook = models.URLField(blank=True)
    picture = models.ImageField(upload_to="OurTeam/", blank=True)


class Course(models.Model):
    title = models.CharField(max_length=20, unique=True, blank=False)
    description = HTMLField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


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
    image = models.ImageField(upload_to="notices/", blank=True)
