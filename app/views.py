from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Info,
    AboutUs,
    AboutUsImage,
    Course,
    Team,
    Gallery,
    GalleryImage,
    Message,
)
from events.models import Event
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings


def index(request):
    info = Info.objects.first()
    courses = Course.objects.all()
    about_us = AboutUs.objects.first()
    portion_of_description = about_us.description[:600]
    events = Event.objects.all()
    msg = Message.objects.all()

    context = {
        "info": info,
        "courses": courses,
        "about_description": portion_of_description,
        "events": events,
        "msg": msg,
    }
    return render(request, "index.html", context)


def about(request):
    about = AboutUs.objects.first()
    about_us_images = AboutUsImage.objects.filter(about=about)
    teams = Team.objects.all()
    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "info": info,
        "about": about,
        "about_us_images": about_us_images,
        "teams": teams,
        "courses": courses,
    }
    return render(request, "about.html", context)


def contact(request):
    full_name = request.POST.get("full-name")
    message = request.POST.get("message")
    sender = request.POST.get("email")
    phone = request.POST.get("phone")
    subject = request.POST.get("subject")

    if subject and message and sender:
        email_message = f"Message: {message}\n\n\nSender: {full_name}\nEmail: {sender}\nPhone Number: {phone}"
        try:
            # Send email
            send_mail(
                subject,
                email_message,
                sender,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            success_message = "Message sent successfully"
            messages.success(request, success_message)
            return redirect("contact")
        except BadHeaderError:
            error_message = "Message failed to send!"
            messages.error(request, error_message)
            return redirect("contact")

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "info": info,
        "courses": courses,
    }
    return render(request, "contact.html", context)


def gallery(request):
    galleries = Gallery.objects.all()

    gallery_data = []
    for gallery in galleries:
        images = GalleryImage.objects.filter(gallery=gallery)
        gallery_data.append({"gallery": gallery, "images": images})

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "gallery_data": gallery_data,
        "info": info,
        "courses": courses,
    }
    return render(request, "gallery.html", context)


def courseDetails(request, course_slug):
    single_course = get_object_or_404(Course, slug=course_slug)

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "course": single_course,
        "info": info,
        "courses": courses,
    }
    return render(request, "course-details.html", context)
