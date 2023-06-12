from django.utils import timezone
from django.conf import settings
from .models import Visitor

from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)
logger.info(__name__)


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        remote_addr = request.META.get('REMOTE_ADDR', '')
        http_referer = request.META.get('HTTP_REFERER', '')

        parsed_referer = urlparse(http_referer)
        block_path = ['/' + settings.DJANGO_ADMIN_URL_PATH,
                      '/static/', '/media/']

        if not any(parsed_referer.path.startswith(path) for path in block_path):
            try:
                Visitor.objects.create(
                    user_agent=user_agent,
                    remote_addr=remote_addr,
                    http_referer=http_referer,
                    timestamp=timezone.now(),
                )
            except Exception as e:
                logger.error(e)

        response = self.get_response(request)

        return response
