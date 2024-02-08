from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Info,
    AboutUs,
    AboutUsImage,
    Course,
    Team,
    Notice,
    NoticeImage,
    Gallery,
    GalleryImage,
)
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings


def index(request):
    info = Info.objects.first()
    courses = Course.objects.all()
    about_us = AboutUs.objects.first()
    portion_of_description = about_us.description[:600]

    context = {
        "info": info,
        "courses": courses,
        "about_description": portion_of_description,
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


def gallery(request):
    galleries = Gallery.objects.all()

    info = Info.objects.first()
    courses = Course.objects.all()

    context = {
        "galleries": galleries,
        "info": info,
        "courses": courses,
    }
    return render(request, "gallery.html", context)


def galleryImages(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)

    context = {"gallery_pictures": gallery}
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
