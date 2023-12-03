from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import EventLog
import json


@csrf_exempt  # Disable CSRF for this view as it's an external API endpoint
@require_http_methods(["POST"])  # Only allow POST requests
def event_listener(request):
    try:
        # Parse the JSON body of the request
        event_data = json.loads(request.body)

        # Assuming event_data is a dictionary containing a list of events
        for event in event_data.get("events", []):
            # Create an EventLog object for each event
            EventLog.objects.create(
                action=event.get("action"),
                author=event.get("author"),
                author_type=event.get("author_type"),
                event_id=event.get("event_id"),
                event_datetime=event.get("event_datetime"),
                pim_source=event.get("pim_source"),
                data=event.get("data"),
            )

        return JsonResponse({"status": "success"}, status=200)

    except Exception as e:
        # Log the error for debugging
        # Here you should log to a file or external logging service
        print(f"Error processing event: {e}")

        return JsonResponse({"status": "error", "message": str(e)}, status=500)
