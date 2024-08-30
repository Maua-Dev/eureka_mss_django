from django.test import TestCase, RequestFactory

from app.views.request_url_views import RequestUrlViews


class Test_DeliveryView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_create_delivery_view(self):
        request = self.factory.post('/request_url', {
            "project_id": 1,
            "upload_type": "mp4",
            "file_name": "video_projeto_1"
            },
            content_type='application/json',
        )

        response = RequestUrlViews.request_url(request)

        assert response.status_code == 200

    def test_create_delivery_view_bad_request(self):
        request = self.factory.post('/request_url', {
            "project_id": 'string',
            "upload_type": "mp4",
            "file_name": "video_projeto_1"
            },
            content_type='application/json',
        )

        response = RequestUrlViews.request_url(request)

        assert response.status_code == 400

    def test_create_delivery_forbidden(self):
        request = self.factory.put('/request_url', {
            "project_id": 1,
            "upload_type": "mp4",
            "file_name": "video_projeto_1"
            },
            content_type='application/json',
        )

        response = RequestUrlViews.request_url(request)
        print(response)

        assert response.status_code == 403



