from rest_framework.views import exception_handler

from utils.formatters import ErrorsFormatter


def exception_errors_format_handler(exc, context):
    response = exception_handler(exc, context)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response

    formatter = ErrorsFormatter(exc)

    response.data = formatter()

    return response
