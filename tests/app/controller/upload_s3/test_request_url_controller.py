from django.test import TestCase

from app.controllers.request_url.request_url_controller import RequestGenerateUrlController
from app.helpers.http.django_http_request import DjangoHttpRequest


class Test_RequestUrlController(TestCase):

    def test_request_url_controller_OK(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "upload_type": "mp4",
                "file_name": "video_projeto_1"
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 200
        assert response.body.get('url') is not None
        assert response.message == 'The presigned url was generated successfully'

    def test_request_url_controller_missing_project_id(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": None,
                "upload_type": "mp4",
                "file_name": "video_projeto_1"
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.message == 'Field project_id is missing for method get_presigned_url'

    def test_request_url_controller_missing_upload_type(self): #Erro aqui
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "upload_type": None,
                "file_name": 'hello'
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.message == 'Field upload_type is missing for method get_presigned_url'

    def test_request_url_controller_missing_file_name(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "upload_type": 'video',
                "file_name": None
            },
            method="POST"
        )

        response = controller(request)

        print(response)

        assert response.status_code == 400
        assert response.message == "Field file_name is missing for method get_presigned_url"

    def test_request_url_controller_missing_multiple_params(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 400

    def test_request_url_controller_method_not_allowed(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "upload_type": "video",
                "file_name": "file_name_1"
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 403
        assert response.message == 'Method POST is not allowed for route get_presigned_url'

    def test_request_url_controller_wrong_type_project_id(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 'affirm',
                "upload_type": "video",
                "file_name": "file_name_1"
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.message == 'Tipo de parâmetro incorreto para project_id'

    def test_request_url_controller_wrong_type_upload_type(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "upload_type": False,
                "file_name": "file_name_1"
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.message == 'Tipo de parâmetro incorreto para upload_type'

    def test_request_url_controller_wrong_type_file_name(self):
        controller = RequestGenerateUrlController()
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "upload_type": 'pdf',
                "file_name": 22112004
            },
            method="POST"
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.message == 'Tipo de parâmetro incorreto para file_name'
