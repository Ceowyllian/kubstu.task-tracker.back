from django.middleware.common import MiddlewareMixin
from request_logging.middleware import LoggingMiddleware

from config.settings.logging import USE_GRAYLOG

__all__ = [
    "ExtractTokenMiddleware",
    "RequestLoggingMiddleware",
]


class ExtractTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        token = request.COOKIES.get("auth_token", None)
        if token:
            request.META["HTTP_AUTHORIZATION"] = f"Token {token}"


class RequestLoggingMiddleware(LoggingMiddleware):
    def _get_logging_context(self, request, response):
        """
        Returns a map with args and kwargs to provide additional context to
        calls to logging.log(). This allows the logging context to be
        created per process request/response call.
        """

        context = super()._get_logging_context(request, response)

        if not USE_GRAYLOG:
            return context

        not_authenticated = "Not Authenticated"

        user = request.user
        user_is_anonymous = user.is_anonymous
        user_is_authenticated = user.is_authenticated
        user_id = user.id or not_authenticated
        user_email = getattr(user, "email", not_authenticated)
        user_is_active = user.is_active
        user_is_staff = user.is_staff
        user_is_superuser = user.is_superuser

        context["kwargs"]["extra"].update(
            {
                "request_user_agent": request.headers.get("User-Agent", None),
                "request_accept_language": request.headers.get("Accept-Language", None),
                "request_path": request.path,
                "request_method": request.method,
                "response_status_code": response.status_code,
                "user_is_anonymous": user_is_anonymous,
                "user_is_authenticated": user_is_authenticated,
                "user_id": user_id,
                "user_email": user_email,
                "user_is_active": user_is_active,
                "user_is_staff": user_is_staff,
                "user_is_superuser": user_is_superuser,
            }
        )
