from django.urls import path
from .views import event_listener

urlpatterns = [
    path("event-listener/", event_listener, name="event-listener"),
]
