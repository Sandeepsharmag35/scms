from django.contrib import admin
from .models import (
    Info,
    AboutUs,
    AboutUsImage,
    Team,
    Course,
    Notice,
    NoticeImage,
    Gallery,
    GalleryImage,
)

# from tinymce.widgets import TinyMCE


# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone_number", "address"]


admin.site.register(Info, InfoAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "post"]


admin.site.register(Team, TeamAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug"]


admin.site.register(Course, CourseAdmin)


class AboutUsImageInline(admin.StackedInline):
    model = AboutUsImage
    extra = 1  # Number of empty forms to display for adding new images


class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInline]


admin.site.register(AboutUs, AboutUsAdmin)


class NoticeImageInline(admin.StackedInline):
    model = NoticeImage
    extra = 1


class NoticeAdmin(admin.ModelAdmin):
    inlines = [NoticeImageInline]


admin.site.register(Notice, NoticeAdmin)


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage
    extra = 3


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]


admin.site.register(Gallery, GalleryAdmin)
