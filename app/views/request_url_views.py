from app.controllers.request_url.request_url_controller import RequestGenerateUrlController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

class RequestUrlViews:

    @staticmethod
    def request_url(request):

        controller = RequestGenerateUrlController()
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()

