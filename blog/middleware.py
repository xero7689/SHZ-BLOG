from django.utils import timezone
from .models import Visitor


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        remote_addr = request.META.get('REMOTE_ADDR', '')
        http_referer = request.META.get('HTTP_REFERER', '')

        Visitor.objects.create(
            user_agent=user_agent,
            remote_addr=remote_addr,
            http_referer=http_referer,
            timestamp=timezone.now(),
        )

        response = self.get_response(request)

        return response
