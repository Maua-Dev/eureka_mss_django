from django.test import TestCase, RequestFactory

from app.views.delivery_views import DeliveryViews


class Test_DeliveryView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_create_delivery_view(self):
        request = self.factory.post('/create_delivery', {
            "task_id": 1,
            "project_id": 1,
            "user_id": 1,
            "content": {"content": "Algum conteúdo"},
        },
        content_type='application/json')

        response = DeliveryViews.create_delivery(request)

        assert response.status_code == 201

    def test_get_deliveries_view(self):
        request = self.factory.get('/get_deliveries?project_id=1',
        content_type='application/json')

        response = DeliveryViews.get_deliveries(request)

        assert response.status_code == 200
