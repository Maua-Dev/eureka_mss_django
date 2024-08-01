from app.helpers.http.django_http_response import DjangoHttpResponse


class StatusViews:

    @staticmethod
    def status(request):
        http_response = DjangoHttpResponse(body={}, message="Eureka API is running", status_code=200)

        return http_response.to_django()
