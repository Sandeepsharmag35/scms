from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("notices/", views.notices, name="notices"),
    path("notices/<str:notice_slug>/", views.noticesDetails, name="notice-details"),
    path("events/", views.events, name="events"),
    path("event-details/<str:event_slug>/", views.eventDetails, name="event-details"),
]


# Serving static & media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
