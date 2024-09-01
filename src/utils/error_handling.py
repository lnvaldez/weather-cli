from http import HTTPStatus
from requests.exceptions import HTTPError

err_url = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/"

error_messages = {
    HTTPStatus.UNAUTHORIZED: "Error 401: Unauthorized. Please check your API key.",
    HTTPStatus.NOT_FOUND: "Error 404: Resource not found. Please check the requested URL.",
    HTTPStatus.TOO_MANY_REQUESTS: "Error 429: Too many requests. Please try again later.",
    HTTPStatus.INTERNAL_SERVER_ERROR: "Error 500: Internal server error. Please try again later.",
    HTTPStatus.BAD_GATEWAY: "Error 502: Bad gateway. Please try again later.",
    HTTPStatus.SERVICE_UNAVAILABLE: "Error 503: Service unavailable. Please try again later.",
    HTTPStatus.GATEWAY_TIMEOUT: "Error 504: Gateway timeout. Please try again later.",
}


def handle_http_error(error: HTTPError):
    status_code = error.response.status_code

    if status_code in error_messages:
        print(error_messages.get(status_code))
    else:
        print(f"Error {status_code}: {err_url + status_code}")
