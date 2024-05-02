from django.shortcuts import render, get_object_or_404
from app.models import Info, Course
from .models import Notice, NoticeImage, Event, EventImage

# Create your views here.


def notices(request):
    notices = Notice.objects.all().order_by("-date")

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "notices": notices,
        "info": info,
        "courses": courses,
    }
    return render(request, "notices.html", context)


def noticesDetails(request, notice_slug):
    single_notice = get_object_or_404(Notice, slug=notice_slug)

    notice_images = NoticeImage.objects.filter(notice=single_notice)

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "notice": single_notice,
        "notice_images": notice_images,
        "info": info,
        "courses": courses,
    }
    return render(request, "notice-details.html", context)


def events(request):
    events = Event.objects.all().order_by("-date")
    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "events": events,
        "info": info,
        "courses": courses,
    }

    return render(request, "events.html", context)


def eventDetails(request, event_slug):
    single_event = get_object_or_404(Event, slug=event_slug)
    event_images = EventImage.objects.filter(event=single_event)

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "event": single_event,
        "event_images": event_images,
        "info": info,
        "courses": courses,
    }
    pass
    return render(request, "event-details.html", context)
