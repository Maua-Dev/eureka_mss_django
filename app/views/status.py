from app.helpers.http.django_http_response import DjangoHttpResponse


class StatusViews:

    @staticmethod
    def status(request):
        http_response = DjangoHttpResponse(body={})

        return http_response.to_django()
