from .models import Visitor

from urllib.parse import urlparse
import logging


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('blog.middleware.visitor_tracking')

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        remote_addr = request.META.get('REMOTE_ADDR', '')

        http_referer = request.META.get('HTTP_REFERER', '')
        parsed_referer = urlparse(http_referer)

        path_info = request.META.get('PATH_INFO', None)

        response = self.get_response(request)
        if response.status_code == 200:
            try:
                Visitor.objects.create(
                    remote_addr=remote_addr,
                    user_agent=user_agent,
                    http_referer=parsed_referer,
                    path_info=path_info,
                )
            except Exception as e:
                self.logger.error(str(e))

        return response
