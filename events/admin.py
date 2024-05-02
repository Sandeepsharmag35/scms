from django.contrib import admin
from .models import Notice, NoticeImage, Event, EventImage


# Register your models here.
class NoticeImageInline(admin.StackedInline):
    model = NoticeImage
    extra = 1


class NoticeAdmin(admin.ModelAdmin):
    inlines = [NoticeImageInline]


admin.site.register(Notice, NoticeAdmin)


class EventImageInline(admin.StackedInline):
    model = EventImage
    extra = 2


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]


admin.site.register(Event, EventAdmin)
